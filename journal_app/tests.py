from django.test import TestCase
from journal_app.models import Posts


class SimpleTestCase(TestCase):
    def test_that_number_is_returned(self):
        self.assertEqual(Posts.num(3), 3)
