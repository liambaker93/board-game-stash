from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.PostList.as_view(), name='list'),
]