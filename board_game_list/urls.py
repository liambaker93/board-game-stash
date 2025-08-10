from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('library/', views.update_library, name='update_library'),
    path('edit/<int:game_id>', views.library_edit, name='edit_library'),
    path('delete/<int:game_id>', views.library_delete, name='delete_library'),
    path('<slug:slug>', views.game_detail, name='full_detail'),
]