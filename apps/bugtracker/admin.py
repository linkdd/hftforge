from django.contrib import admin
from apps.bugtracker.models import Milestone, Issue

admin.site.register(Milestone)
admin.site.register(Issue)
