from django.test import TestCase
from django.urls import reverse
from re_domain.find_domains import find_domains

class FindDomainFuncTests(TestCase):
    def test_func_correct(self):
        actual = find_domains('sunday@november.ru')
        expected = '@november.ru'
        self.assertEquals(actual, expected)
    def test_func_incorrect(self):
        actual = find_domains('sunday_november.ru')
        expected = 'Incorrect string'
        self.assertEquals(actual, expected)