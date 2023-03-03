from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.LoginView.as_view(), name='login'),
  path('logout/', views.LogoutView.as_view(), name='api-logout'),
  path('session/', views.SessionView.as_view(), name='api-session'),
  path('whoami/', views.WhoAmIView.as_view(), name='api-whoami'),
]

