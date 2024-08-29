from django.contrib import admin
from tudu_app.models import *

# Register your models here.
admin.site.register([user_data,task_type_lists,tasks_data])