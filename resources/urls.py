from django.urls import path
from .views import upload_resource, download_resource, group_resources

urlpatterns = [
    path('upload/<int:group_id>/', upload_resource, name='upload_resource'),        
    path('download/<int:resource_id>/', download_resource, name='download_resource'), 
    path('group/<int:group_id>/resources/', group_resources, name='group_resources'),
                  
]
