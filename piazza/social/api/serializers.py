from rest_framework import serializers

from social.models import Post


class PostSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField('get_username_from_author')

    class Meta:
        model = Post
        fields = ['id', 'title', 'topic', 'created', 'body', 'expiration', 'username']

    def get_username_from_author(self, post):
        username = post.author.username
        return username
