from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import ToDoList, ToDoItem


class ToDoListView(ListView):
    model = ToDoList
    template_name = 'todoapp/index.html'
    
    
class ToDoItemListView(ListView):
    model = ToDoItem
    template_name = 'todoapp/list.html'
    
    
    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs['list_id'])
    
    
    def get_context_data(self):
        context = super().get_context_data()
        context['todo_list'] = ToDoList.objects.get(id=self.kwargs['list_id'])
        return context
    
    
class ToDoListCreateView(CreateView):
    model = ToDoList
    fields = ['title']
    
    
    def get_context_data(self):
        context = super().get_context_data()
        context['title'] = 'Add a new list'
        return context
    
    
class ToDoItemCreateView(CreateView):
    model = ToDoItem
    fields = ['todo_list', 'title', 'description', 'due_date']


    def get_context_data(self):
        context = super().get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs['list_id'])
        context['todo_list'] = todo_list
        return context
    
    
    def get_success_url(self):
        return reverse('todoapp:list', args=[self.object.todo_list_id])
    
    
class ToDoItemUpdateView(UpdateView):
    model = ToDoItem
    fields = ['todo_list', 'title', 'description', 'due_date']
    
    
    def get_context_data(self):
        context = super().get_context_data()
        context['todo_list'] = self.object.todo_list
        context['title'] = 'Edit item'
        return context
    
    
    def get_success_url(self):
        return reverse('todoapp:list', args=[self.object.todo_list_id])
    
    
class ToDoListDeleteView(DeleteView):
    model = ToDoList
    success_url = reverse_lazy('todoapp:index')
    
    
class ToDoItemDeleteView(DeleteView):
    model = ToDoItem
    
    
    def get_success_url(self):
        return reverse_lazy('todoapp:list', args=[self.kwargs['list_id']])
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_list'] = self.object.todo_list
        return context