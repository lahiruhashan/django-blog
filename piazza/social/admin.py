from django.contrib import admin

from social.models import Post, Comment, Like, Dislike

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dislike)
