from django.urls import resolve
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import RequestsClient
import logging 

 
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)

class HomePageTest(TestCase):

    def test_root_url_resolves_to_CountryPost_view(self):
        client = RequestsClient()
        response = client.post('http://localhost:9090/Country/', {'name': 'TEST'})
        print(response)
        self.assertTrue(str(response).find("405")>-1)

    def test_root_url_resolves_to_CountryPut_view(self):
        client = RequestsClient()
        response = client.put('http://localhost:9090/Country/3/', {'name': 'TEST2'})
        print(response)
        self.assertTrue(str(response).find("404")>-1)

    def test_root_url_resolves_to_CountryList_view(self):
        client = RequestsClient()
        response = client.get('http://localhost:9090/Countries')
        print(response)
        self.assertEqual(response.status_code, 200)
