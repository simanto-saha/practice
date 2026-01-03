from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_data, name='show_data'),
    path('check_api/', views.check_api, name='check_api'),
]