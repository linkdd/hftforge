from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField()
    homepage = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name
