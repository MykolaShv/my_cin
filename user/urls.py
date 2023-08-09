from django.urls import path
from .views import profile, Register, Login, Logout, PasswordChange

urlpatterns = [
    path('profile/<str:username>/', profile, name='profile'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
