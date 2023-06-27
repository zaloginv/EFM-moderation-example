from django.urls import path
from .views import RegisterView, ProfileView, AuthLoginView, AuthLogoutView

app_name = 'auth-app'

urlpatterns = [
    path('login/', AuthLoginView.as_view(), name='login'),
    path('logout/', AuthLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile')
]