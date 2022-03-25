from django.test import TestCase, Client
from .models import Posts, Quotes


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class PostsModelTest(TestCase):

    def testPostExists(self):
        post = Posts.objects.create(
            title='day at park', content='I went to the park', img_link="some link")

        self.assertEqual(str(post.title), 'day at park')
        self.assertEqual(str(post.content), 'I went to the park')
        self.assertEqual(str(post.img_link), 'some link')

    def test_verbose_name_plural(self):
        self.assertEqual(str(Posts._meta.verbose_name_plural), "Posts")


class QuotesModelTest(TestCase):
    def testQuoteExists(self):
        quote = Quotes.objects.create(
            title='clueless', content='As If!', img_link="some link")

        self.assertEqual(str(quote.title), 'clueless')
        self.assertEqual(str(quote.content), 'As If!')
        self.assertEqual(str(quote.img_link), 'some link')

    def test_verbose_name_plural(self):
        self.assertEqual(str(Quotes._meta.verbose_name_plural), "Quotes")


class AllRoutesTest(TestCase):

    def testHomeRoute(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def testPostsRoute(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def testQuotesRoute(self):
        response = self.client.get('/quotes/')
        self.assertEqual(response.status_code, 200)

    def testPostsPostRequest(self):
        response = self.client.post(
            '/quotes/', {'title': 'clueless', 'content': 'As if!', 'img_link': 'an img of cher'})
        self.assertEqual(response.status_code, 201)

    def testQuotesPostRequest(self):
        response = self.client.post(
            '/quotes/', {'title': 'trip to athens', 'content': 'I saw the acropolis !!!', 'img_link': 'an img of the acropolis'})
        self.assertEqual(response.status_code, 201)
