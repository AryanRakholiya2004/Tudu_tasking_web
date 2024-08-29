from django.db import models
from allauth.socialaccount.models import SocialAccount
from django import forms

# Create your models here.
class user_data(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=100)
    user_loged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class task_type_lists(models.Model):
    list = models.CharField(max_length=100)
    added_by = models.ForeignKey(user_data,on_delete=models.CASCADE,default=0)
    added_by_google = models.ForeignKey(SocialAccount,on_delete=models.CASCADE,default=0)
    task_modified = models.DateTimeField(auto_now_add=True)
    is_google = models.BooleanField(default=False)

    def __str__(self):
        return self.list
    
class tasks_data(models.Model):
    task_title = models.CharField(max_length=250)
    task_desc = models.TextField()
    task_modified = models.DateTimeField(auto_now_add=True)
    list_name = models.ForeignKey(task_type_lists,on_delete=models.CASCADE)
    added_by = models.ForeignKey(user_data,on_delete=models.CASCADE,default=0)
    added_by_google = models.ForeignKey(SocialAccount,on_delete=models.CASCADE,default=0)
    is_google = models.BooleanField(default=False)

    def __str__(self):
        return self.task_title

class task_form(forms.ModelForm):
    class Meta:
        model = tasks_data
        fields = ['task_title','task_desc','list_name','added_by']