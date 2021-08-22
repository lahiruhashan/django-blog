from django.conf import settings
from django.db import models
from django.db.models import UniqueConstraint


class Post(models.Model):
    TOPICS = (
        ('TECH', 'Tech'),
        ('POLITICS', 'Politics'),
        ('HEALTH', 'Health'),
        ('SPORT', 'Sport'),
    )

    title = models.CharField(max_length=30)
    topic = models.CharField(max_length=10, choices=TOPICS)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    expiration = models.DateTimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Like(models.Model):
    UniqueConstraint(fields=['post', 'author'], name='like_comp_key')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Dislike(models.Model):
    UniqueConstraint(fields=['post', 'author'], name='dislike_comp_key')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
