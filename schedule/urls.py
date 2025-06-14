from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:group_id>/', views.create_session, name='create_session'),

    path('list/<int:group_id>/', views.session_list, name='session_list'),
]


