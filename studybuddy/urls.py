from django.contrib import admin
from django.urls import path, include
from users import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  
    path('studygroups/', include('studygroups.urls')),
    path('chat/', include('chat.urls')),
    path('', views.home, name='home'),





]

