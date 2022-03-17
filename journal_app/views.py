from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import PostSerializer, QuoteSerializer
from .models import Posts, Quotes


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('title')
    serializer_class = PostSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quotes.objects.all().order_by('title')
    serializer_class = QuoteSerializer
