from django.contrib import admin
from django.urls import path, include
from users import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  
    path('studygroups/', include('studygroups.urls')),
    path('chat/', include('chat.urls')),
    path('', views.home, name='home'),   
    path('resources/', include('resources.urls')),
    path('schedule/', include('schedule.urls')),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

