from django.urls import path, include

from .views import index_view, dashboard_view, create_mushroom_view, create_category_view, delete_mushroom_view, details_mushroom_view, edit_mushroom_view

urlpatterns = [
    path('', index_view, name='index'),
    path('create-category/', create_category_view, name='create_category'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('create-mushroom/', create_mushroom_view, name='create_mushroom'),
    path('<int:pk>/', include([
        path('details-mushroom/', details_mushroom_view, name='details_mushroom'),
        path('edit-mushroom/', edit_mushroom_view, name='edit_mushroom'),
        path('delete-mushroom/', delete_mushroom_view, name='delete_mushroom'),
    ]))
]