from django.urls import path, include

from apps.core.views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup")
]
