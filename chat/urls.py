from django.urls import path
from . import views

urlpatterns = [
    path('group/<int:group_id>/', views.group_chat, name='group_chat'),
]
