from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import permissions, status, generics, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .serializers import ExerciseSerializer, DeviceSerializer, ListDatumSerializer
from ..core.models import Datum, Exercise, Device


class DeviceView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            obj = self.queryset.get(uid=self.kwargs["uid"])
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        data = self.serializer_class(obj).data
        return Response({"Device Exists"}, status=status.HTTP_200_OK)


class ExerciseCreate(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ExerciseSerializer
    allowed_methods = ("POST",)
    queryset = Exercise.objects.all()


class DatumCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ListDatumSerializer
    allowed_methods = ("POST",)
    queryset = Datum.objects.all()
