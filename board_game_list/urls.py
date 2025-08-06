from django.urls import path
from . import views


urlpatterns = [
    # path('', views.PostList.as_view(), name='list'),
    path('', views.update_library, name='update_library'),
]