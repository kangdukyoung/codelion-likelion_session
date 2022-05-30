from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('<int:blog_id>/delete', views.delete, name='delete'),
    path('<int:blog_id>/update', views.update, name='update'),
]
