# from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase
from django.contrib.auth.models import AnonymousUser
from .views import FlightView


# Create your tests here.
class FlightTestCase(APITestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_flight_list_as_guest_user(self):
        request = self.factory.get('/flight/flights/')
        request.user = AnonymousUser()
        response = FlightView.as_view({'get': 'list'})(request)
        self.assertEquals(response.status_code, 200)
