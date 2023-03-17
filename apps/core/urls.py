from django.urls import path, include

from apps.core import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
