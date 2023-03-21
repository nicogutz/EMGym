from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework import serializers

from apps.core.models import Datum, Exercise, Device


class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """

    username = serializers.CharField(label="Username", write_only=True)

    password = serializers.CharField(
        label="Password",  # This will be used when the DRF browsable API is enabled
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get("username")
        password = attrs.get("password")

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = "Access denied: wrong username or password."
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code="authorization")
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs["user"] = user
        return attrs


class DeviceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    uid = serializers.CharField(label="uid", required=True, max_length=10)

    class Meta:
        model = Device
        fields = ("uid", "user")

    def perform_create(self, serializer):
        serializer.save(user=self.context["user"])


class ExerciseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    muscle = serializers.ChoiceField(
        choices=Exercise.ExerciseType.choices, default=Exercise.ExerciseType.NA
    )
    timestamp = serializers.DateTimeField(required=True)
    repetitions = serializers.IntegerField(label="repetitions", required=True)
    exertion_value = serializers.FloatField(label="exertion_value", required=True)
    uid = serializers.CharField(write_only=True)

    class Meta:
        model = Exercise
        fields = ("id", "uid", "muscle", "repetitions", "exertion_value", "timestamp")

    def create(self, validated_data):
        device = Device.objects.get(uid=validated_data.pop("uid"))
        exercise = Exercise.objects.create(device=device, **validated_data)
        return exercise


class DatumSerializer(serializers.ModelSerializer):
    data_count = serializers.IntegerField(label="data_count", required=True)
    value = serializers.FloatField(label="value", required=True)
    exercise_id = serializers.IntegerField(required=True)

    class Meta:
        model = Datum
        # list_serializer_class = ListDatumSerializer(many=True)
        fields = (
            "exercise_id",
            "data_count",
            "value",
        )


class ListDatumSerializer(serializers.ListSerializer):
    child = DatumSerializer()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        exercise = Exercise.objects.get(pk=validated_data[0].get("exercise_id"))

        from scipy.signal import savgol_filter, find_peaks
        from scipy import integrate
        import pandas as pd

        df = pd.DataFrame(validated_data)
        df.value = savgol_filter(df.value.rolling(3).mean(), 12, 3)
        df.value = df.value.fillna(0)

        exercise.repetitions = find_peaks(df.value, prominence=0.1)[0].size
        exercise.exertion_value = (
            integrate.trapz(df.value, df.data_count) / exercise.repetitions
        )

        exercise.save()

        result = [Datum.objects.create(**datum) for datum in df.to_dict("records")]

        try:
            self.child.Meta.model.objects.bulk_create(result, ignore_conflicts=True)
        except IntegrityError as e:
            raise ValidationError(e)

        return result
