from django.contrib.auth import authenticate
from django.contrib.auth.models import User
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

    password = serializers.CharField(label="Password",  # This will be used when the DRF browsable API is enabled
                                     style={'input_type': 'password'}, trim_whitespace=False, write_only=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs


class DeviceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    uid = serializers.CharField(label="uid", required=True, max_length=10)

    class Meta:
        model = Device
        fields = ('uid', 'user')

    def perform_create(self, serializer):
        serializer.save(user=self.context['user'])


class ExerciseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    muscle = serializers.ChoiceField(choices=Exercise.ExerciseType.choices, default=Exercise.ExerciseType.NA)
    repetitions = serializers.IntegerField(label="repetitions", required=True)
    exertion_value = serializers.FloatField(label="exertion_value", required=True)
    uid = serializers.CharField(write_only=True)

    class Meta:
        model = Exercise
        fields = ('id', 'uid', 'muscle', 'repetitions', 'exertion_value')

    def create(self, validated_data):
        device = Device.objects.get(uid=validated_data.pop('uid'))
        exercise = Exercise.objects.create(device=device, **validated_data)
        return exercise


class DatumSerializer(serializers.ModelSerializer):
    data_count = serializers.IntegerField(label="data_count", required=True)
    value = serializers.FloatField(label="value", required=True)
    exercise_id = serializers.IntegerField(required=True)

    class Meta:
        model = Datum
        fields = ('exercise_id', 'data_count', 'value',)

    def create(self, validated_data):
        exercise = Exercise.objects.get(pk=validated_data.pop('exercise_id'))
        datum = Datum.objects.create(exercise=exercise, **validated_data)
        return datum
