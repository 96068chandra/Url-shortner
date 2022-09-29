from django.urls import path
from . import views

urlpatterns = [
    path('',views.Front,name='Front'),
    path('create',views.create,name='create'),
    path('<str:pk>',views.go,name='go')

]