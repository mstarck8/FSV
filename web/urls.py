from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('Training/', views.training, name='training'),
    path('Kontakt/', views.contact_view, name='contact'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('Maischwimmen/', views.maischwimmen, name='ms'),
    path('Trainingslager/', views.trainingslager, name='tl'),
]
