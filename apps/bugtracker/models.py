from django.db import models
from django.contrib.auth.models import User

from apps.post.models import Post

class Milestone(models.Model):
    name = models.CharField(max_length=25)
    duetime = models.DateTimeField()
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Issue(Post):
    STATE_CHOICES = (
        ('O', 'Open'),
        ('C', 'Closed'),
        ('F', 'Fixed'),
    )

    assigned = models.ForeignKey(User)
    milestone = models.ManyToManyField(Milestone)
    duetime = models.DateTimeField()
    state = models.CharField(max_length=1, choices=STATE_CHOICES)
