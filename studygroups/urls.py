from django.urls import path
from . import views

urlpatterns = [
    
    path('create/', views.create_study_group, name='create_group'),

   
    path('groups/', views.group_list, name='group_list'),

    
    path('join/<int:group_id>/', views.join_group, name='join_group'),

   
    path('group/<int:group_id>/', views.group_details, name='group_details'),

   
    path('leave/<int:group_id>/', views.leave_group, name='leave_group'),
]
