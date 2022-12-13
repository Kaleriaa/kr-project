from django.urls import reverse
from rest_framework.test import APITestCase


class FindDomainTests(APITestCase):
    def test_find_incorrect(self):
        url = reverse('searcher', args=['aaaa_vk10'])
        response = self.client.get(url)
        self.assertEquals(response.data, {
            "text": "aaaa_vk10",
            "result": "Incorrect string"
        })
    def test_find_incorrect_domain(self):
        url = reverse('searcher', args=['aaaa_vk10@mail.ru@fpfpf.cc'])
        response = self.client.get(url)
        self.assertEquals(response.data, {
            "text": "aaaa_vk10@mail.ru@fpfpf.cc",
            "result": "@mail.ru"
        })
    def test_find_correct(self):
        url = reverse('searcher', args=['aaaa_vk10@mail.ru'])
        print(url)
        response = self.client.get(url)
        self.assertEquals(response.data, {
            "text": "aaaa_vk10@mail.ru",
            "result": "@mail.ru"
        })
    