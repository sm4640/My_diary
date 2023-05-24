from django.urls import path

from . import views

urlpatterns = [
    path('', views.diary_list, name = 'diary_list'),
    path('<int:pk>', views.diary_detail, name = 'diary_detail'),
    path('post/', views.diary_post, name='diary_post'),
    path('<int:pk>/edit/', views.diary_edit, name='diary_edit'),
    path('<int:pk>/delete/', views.diary_delete, name='diary_delete'),
]