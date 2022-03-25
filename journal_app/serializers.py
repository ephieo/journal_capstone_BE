from rest_framework import serializers
from .models import Posts, Quotes


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ("id", "title", "content")


class QuoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quotes
        fields = ("id", "title", "content", "img_link")
