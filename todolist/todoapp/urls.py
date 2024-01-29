from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.ToDoListView.as_view(), name='index'),
    path('list/<int:list_id>', views.ToDoItemListView.as_view(),
         name='list'),
    path('list/add/', views.ToDoListCreateView.as_view(),
         name='list_add'),
    path('list/<int:list_id>/item/add/', views.ToDoItemCreateView.as_view(),
         name='item_add'),
    path('list/<int:list_id>/item/<int:pk>/', 
         views.ToDoItemUpdateView.as_view(),
         name='item_update'),
    path('list/<int:pk>/delete/', views.ToDoListDeleteView.as_view(),
         name='list_delete'),
    path('list/<int:list_id>/item/<int:pk>/delete/', 
         views.ToDoItemDeleteView.as_view(),
         name='item_delete')
]
