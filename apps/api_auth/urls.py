from django.urls import path
from . import views

urlpatterns = [
  path('user/login/', views.LoginView.as_view(), name='login'),
  path('user/logout/', views.LogoutView.as_view(), name='api-logout'),
  path('user/session/', views.SessionView.as_view(), name='api-session'),
  path('user/whoami/', views.WhoAmIView.as_view(), name='api-whoami'),

  path('core/device/<int:uid>', views.DeviceView.as_view(), name='device'),
  path('core/exercise/', views.ExerciseCreate().as_view(), name='exercise_create'),
  path('core/datum/', views.DatumCreate().as_view(), name='data_create'),

  # path('view-data/', views.DatumView().as_view(), name='data_view'),
  # path('delete-data/<str:data_count>/', views.DatumDestroy().as_view(), name='data_delete'),
  #
  # path('view-exercise/', views.ExerciseView().as_view(), name='exercise_view'),
  # path('delete-exercise/<str:pk>/', views.ExerciseDestroy().as_view(), name='exercise_delete'),
  #
  # path('create-device/', views.DeviceCreate().as_view(), name='device_create'),
  # path('view-device/', views.DeviceView().as_view(), name='device_view'),
  # path('delete-device/<str:uid>/', views.DeviceDestroy().as_view(), name='device_delete'),

]

