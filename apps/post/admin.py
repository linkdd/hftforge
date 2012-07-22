from django.contrib import admin
from apps.post.models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
