from django.db import models
from django.utils import timezone
from django.urls import reverse


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class ToDoList(models.Model):
    title = models.CharField(max_length=100)
    
    
    def get_absolute_url(self):
        return reverse('todoapp:list', args=[self.id])
    
    
    def __str__(self):
        return self.title
    
    
class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, related_name='todos',
                                  on_delete=models.CASCADE)
    
    
    def get_absolute_url(self):
        return reverse(
            'todoapp:item_update', args=[str(self.todo_list.id), str(self.id)])
        
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering = ['due_date']