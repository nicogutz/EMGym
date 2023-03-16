from django.contrib.auth import login, logout
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions, status, generics, mixins
from rest_framework.generics import GenericAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, \
    CreateAPIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from . import serializers
from .serializers import ExerciseSerializer, DeviceSerializer, DatumSerializer

# dario

from ..core.models import Datum, Exercise, Device


class SessionView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        return JsonResponse({'isAuthenticated': True})


class WhoAmIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        return JsonResponse({'username': request.user.username, 'id': request.user.id})


class LogoutView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = [permissions.AllowAny]
    allowed_methods = ('POST',)

    @staticmethod
    def post(request):
        if not request.user.is_authenticated:
            return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

        logout(request)
        return JsonResponse({'detail': 'Successfully logged out.'})


class LoginView(generics.GenericAPIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.LoginSerializer
    allowed_methods = ('POST',)

    def post(self, request):
        serializer = serializers.LoginSerializer(data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)


class DeviceView(mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            obj = self.queryset.get(uid=self.kwargs['uid'])
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        data = self.serializer_class(obj).data
        return Response(data, status=status.HTTP_200_OK)


class ExerciseCreate(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ExerciseSerializer
    allowed_methods = ('POST',)
    queryset = Exercise.objects.all()
#
#
# class ExerciseView(ListAPIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = ExerciseSerializer
#     allowed_methods = ('POST',)
#     queryset = Exercise.objects.all()
#
#
# class ExerciseDestroy(DestroyAPIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = ExerciseSerializer
#     allowed_methods = ('DELETE', 'GET')
#
#     def get_object(self):
#         queryset = Exercise.objects.all()
#         obj = queryset.get(device_id=self.kwargs['pk'])
#         return obj
#
#
# class ExerciseUpdate(UpdateAPIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = ExerciseSerializer
#     allowed_methods = ('POST',)
#     queryset = Exercise.objects.all()

class DatumView(mixins.CreateModelMixin,
                generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = DatumSerializer
    allowed_methods = ('POST',)
    queryset = Datum.objects.all()

    def post(self, request, *args, **kwargs):
        pass


# class DatumCreate(CreateAPIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = DataSerializer
#     allowed_methods = ('POST',)
#     queryset = Datum.objects.all()
#
#
# class DatumView(ListAPIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = DataSerializer
#     allowed_methods = ('POST', 'GET')
#     queryset = Datum.objects.all()
#
#
# class DatumDestroy(DestroyAPIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = DataSerializer
#     allowed_methods = ('DELETE', 'GET')
#
#     def get_object(self):
#         queryset = Datum.objects.all()
#         obj = queryset.get(data_count=self.kwargs['data_count'])
#         return obj
#
#

