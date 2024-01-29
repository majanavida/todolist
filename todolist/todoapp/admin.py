from django.contrib import admin
from .models import ToDoItem, ToDoList


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['title']
    
    
@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'due_date', 'todo_list']
    list_filter = ['created', 'due_date']