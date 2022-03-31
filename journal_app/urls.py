from django.urls import path
from graphene_django.views import GraphQLView
from journal_app.schema import schema
from django.views.decorators.csrf import csrf_exempt

from django.urls import include, path
# from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'quotes', views.QuoteViewSet)


urlpatterns = [
    # only need the single url too access graphql
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path("graphql", csrf_exempt(GraphQLView.as_view())),
]
