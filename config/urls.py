"""django_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.core.views import HomeView

schema_view = get_schema_view(
    openapi.Info(
        title="EM-Gym API",
        default_version='v1',
        description="The api docs for EM-Gym",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="nicolas.gutierrezsuarez@student.kuleuven.be"),
        license=openapi.License(name="All rights reserved"),
    ),
    public=False,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("apps.core.urls")),  # new
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('apps.api_auth.urls')),
    re_path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('api/v1/core/', include('apps.core.urls')),
    path('', HomeView.as_view(), name="home"),  # new
]

