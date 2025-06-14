from django.urls import path
from .views import upload_resource

urlpatterns = [
    path('upload/<int:group_id>/', upload_resource, name='upload_resource'),
]
