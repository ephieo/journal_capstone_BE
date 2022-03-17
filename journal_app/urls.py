from django.urls import path
from graphene_django.views import GraphQLView
from journal_app.schema import schema


urlpatterns = [
    # only need the single url too access graphql
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema))
]
