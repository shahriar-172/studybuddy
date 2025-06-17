from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),  # ✅ Welcome page (before login)
    path('register/', views.register, name='register'),  # ✅ Registration page
    path('home/', views.home, name='home'),  # ✅ Dashboard after login

    # ✅ Login & Logout using built-in views with custom templates
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
