import graphene
from graphene_django import DjangoObjectType
from .models import Posts


class PostType(DjangoObjectType):
    class Meta:
        model = Posts
        fields = ("id", "title", "content")


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)


schema = graphene.Schema(query=Query)
