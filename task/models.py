from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    bio = models.TextField()
    image = models.ImageField(upload_to='user-images', )

    def __str__(self):
        return f'{self.username}'

class Project(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_projects')
    members = models.ManyToManyField(CustomUser, related_name='member_projects')

    def __str__(self):
        return f'{self.title}'
    
class Task(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    deadline_date = models.DateField() 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned_tasks')
    completed = models.BooleanField(default=False)   

    def __str__(self):
        return f'{self.title}'
    
