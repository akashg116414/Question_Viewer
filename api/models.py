from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
# Create your models here.
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey('group', models.DO_NOTHING)
    comment = models.CharField(max_length=200)
    question = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)

    def __str__(self):
	    return str(self.question)

    class Meta:
        db_table = "question"

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    flag = models.IntegerField(default=1)

    def __str__(self):
	    return self.name

    class Meta:
        db_table = "group"

def document_pre_save_signal(sender, instance, *args, **kwargs):
	if not instance.name:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(document_pre_save_signal, sender=Group)
