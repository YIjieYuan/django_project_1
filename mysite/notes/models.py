# Create your models here.
import datetime

from django.db import models

#20191013 admin删除数据库文件的同时删除media中的文件
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

import os
import uuid

from unidecode import unidecode
from django.template.defaultfilters import slugify

def user_directory_path(instance, filename):# Rename the file
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("files", filename)


class Note(models.Model):
    author = models.CharField('author', max_length=15, default='Yijie Yuan')
    title = models.CharField('title', max_length=200, unique=True)
    category = models.CharField('category', max_length=200, null=True)
    body = models.TextField('body', )
    # pub_date = models.DateTimeField('pub_date', null=True)
    # file = models.FileField(upload_to=user_directory_path, null=True)
    # slug = models.SlugField('slug', max_length=60, blank=True)
    # create_date = models.DateTimeField('create_date', auto_now_add=True)
    # mod_date = models.DateTimeField('mode_date', auto_now=True)
    # status = models.CharField('status', max_length=1, choices=STATUS_CHOICES, default='p')
    # views = models.PositiveIntegerField('views', default=0)
    # category = models.ForeignKey('Category', verbose_name='category', on_delete=models.CASCADE, blank=False, null=False)
    # tags = models.ManyToManyField('Tag', verbose_name='tag', blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.id or not self.slug:
    #         # Newly created object, so set slug
    #         self.slug = slugify(unidecode(self.title))
    #         super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# @receiver(pre_delete, sender=Note)
# def mymodel_delete(sender, instance, **kwargs):
#     # Pass false so FileField doesn't save the model.
#     instance.file.delete(False)


