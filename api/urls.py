from django.urls import path
from .views import UserCreateAPIView,PackagesListView,MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view() , name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('packages/', PackagesListView.as_view(), name='packages'),

]