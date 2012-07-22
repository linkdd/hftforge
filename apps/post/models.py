from django.db import models

from django.contrib.auth.models import User

from apps.tagging.models import Tag
from apps.projects.models import Project

class Post(models.Model):
    author = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    timestamp = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title

class Comment(Post):
    parent = models.ForeignKey(Post)
