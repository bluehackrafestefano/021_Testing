# from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase


# Create your tests here.
class FlightTestCase(APITestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_flight_list_as_guest_user(self):
        request = self.factory.get('/flight/flights/')
        