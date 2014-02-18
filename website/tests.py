from django.test import TestCase
from website.models import FoodTruck

class FoodTruckViewsTestCase(TestCase):
    def test_update_foodtrucks(self):
        res = self.client.get('/foodtrucks/')
        self.assertEqual(res.status_code, 200)

class FoodTruckTestCase(TestCase):
    def setUp(self):
        FoodTruck.objects.create(name = 'vendor1',
                                 location = 'loc1',
                                 start_date = '2014-04-11',
                                 )       


