from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase


class FindDomainTests(APITestCase):
    def test_find_correct(self):
        url = reverse('searcher', )