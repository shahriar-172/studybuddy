from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_study_group, name='create_group'),
    path('groups/', views.group_list, name='group_list'),  # next step
    path('join/<int:group_id>/', views.join_group, name='join_group'),
    path('details/<int:group_id>/', views.group_details, name='group_details'),
    

    

    


]
