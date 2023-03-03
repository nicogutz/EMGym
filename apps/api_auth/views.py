from django.contrib.auth import login, logout
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from . import serializers


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


class LoginView(GenericAPIView):
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
