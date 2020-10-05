from django.urls import path
from . import views

urlpatterns = [
    path('', views.task, name='task'),
    path('listing/', views.liste, name='listing'),
    path('detail/<int:cid>', views.detail, name='detail'),
    path('edit/<int:pers_id>', views.edit, name='edite'),
    path('del/<int:pers_id>', views.delete, name='delete'),
    path('user/<int:user_id>', views.liste_user, name='userlisting'),
]