from django.contrib import admin

# Register your models here.
from .models import Question, Group

admin.site.register(Question)
admin.site.register(Group)