from django.urls import path
from .views import UserRegisterView
# from . import views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
]
