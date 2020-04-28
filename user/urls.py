from django.urls import path

from user import views

urlpatterns = [
    # user registration url
    path('register/', views.UserRegistration.as_view(), name='user_registration'),
    # user login url
    path('login/', views.Login.as_view(), name='user_login'),
]
