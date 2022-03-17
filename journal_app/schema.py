import graphene
from graphene_django import DjangoObjectType
from .models import Posts, Quotes


class PostType(DjangoObjectType):
    class Meta:
        model = Posts
        fields = ("id", "title", "content")


class QuoteType(DjangoObjectType):
    class Meta:
        model = Quotes
        fields = ("id", "title", "content")


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    all_quotes = graphene.List(QuoteType)
    post = graphene.Field(PostType, id=graphene.Int())
    quote = graphene.Field(QuoteType, id=graphene.Int())

    def resolve_all_posts(root, info):
        return Posts.objects.all()

    def resolve_all_quotes(root, info):
        return Quotes.objects.all()

    def resolve_post(root, info, id):
        return Posts.objects.get(pk=id)

    def resolve_quote(root, info, id):
        return Quotes.objects.get(pk=id)


schema = graphene.Schema(query=Query)
