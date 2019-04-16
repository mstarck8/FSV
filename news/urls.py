from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('timeline/', views.timeline_view, name='timeline'),
    path('create/', views.create_view, name='create'),
    path('artikel/<int:post_id>', views.artikel_view, name='artikel'),
    path('artikel/<int:post_id>/delete', views.delete_view, name='delete'),
]
