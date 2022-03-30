from unicodedata import category
from urllib.request import Request
import graphene
from graphene_django import DjangoObjectType
from .models import Posts, Quotes


class PostType(DjangoObjectType):
    class Meta:
        model = Posts
        fields = ("id", "title", "date", "content")


class QuoteType(DjangoObjectType):
    class Meta:
        model = Quotes
        fields = ("id", "title", "date", "content")


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


class AddQuoteMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)

    quote = graphene.Field(QuoteType)

    @classmethod
    def mutate(cls, root, info, title):
        quote = Quotes(title=title)
        quote.save()
        return AddQuoteMutation(quote=quote)


class AddPostMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, title, content):
        post = Posts(title=title, content=content)
        post.save()
        return AddPostMutation(post=post)


class UpdatePostMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String(required=True)

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, title, id):
        post = Posts.objects.get(id=id)
        post.title = title
        post.save()
        return UpdatePostMutation(post=post)


class UpdateQuoteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        title = graphene.String(required=True)

    quote = graphene.Field(QuoteType)

    @classmethod
    def mutate(cls, root, info, title, id):
        quote = Quotes.objects.get(id=id)
        quote.title = title
        quote.save()
        return UpdateQuoteMutation(quote=quote)


class DeletePostMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, id):
        post = Posts.objects.get(id=id)
        post.delete()
        return


class DeleteQuoteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    quote = graphene.Field(QuoteType)

    @classmethod
    def mutate(cls, root, info, id):
        quote = Quotes.objects.get(id=id)
        quote.delete()
        return


class Mutation(graphene.ObjectType):
    add_post = AddPostMutation.Field()
    add_quote = AddQuoteMutation.Field()
    update_post = UpdatePostMutation.Field()
    update_quote = UpdateQuoteMutation.Field()
    delete_post = DeletePostMutation.Field()
    delete_quote = DeleteQuoteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
