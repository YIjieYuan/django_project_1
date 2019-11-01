# Create your models here.
import datetime

from django.db import models
from uuslug import slugify


class Note(models.Model):
    author = models.CharField('author', max_length=15, default='Yijie Yuan')
    pub_date = models.DateTimeField('pub_date', default=datetime.datetime.now, null=True)
    title = models.CharField('title', max_length=200, unique=True)
    category = models.CharField('category', max_length=200, null=True)
    sup_category = models.CharField('sup_category', max_length=200, blank=True)
    sub_category = models.CharField('sub_category', max_length=200, blank=True)
    body = models.TextField('body', )
    slug = models.SlugField('slug', max_length=60, blank=True, unique=True)
    views = models.PositiveIntegerField('views', default=0)
    likes = models.PositiveIntegerField('likes', default=0)

    def save(self, *args, **kwargs):
        # if not self.id:
        # Newly created object, so set slug
        self.slug = slugify(self.title)
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "note"




