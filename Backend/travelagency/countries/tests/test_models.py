from django.test import TestCase
from ..models import Country

# class Country(models.Model):
#     name = models.CharField(max_length=100)
#     currency = models.CharField(max_length=100)
#     symbol = models.CharField(max_length=100)
#     centseparator = models.CharField(max_length=100)
#     millionseparator = models.CharField(max_length=100)
#     locale = models.CharField(max_length=100)
#     decimals = models.CharField(max_length=100)
#     displaysymbol = models.CharField(max_length=100)


class CountryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Country.objects.create(name='POR', currency='EUR')


    def test_name_max_length(self):
        country = Country.objects.get(name="POR")
        max_length = country._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_currency(self):
        country = Country.objects.get(name="POR")
        expected_object_name = country.currency
        self.assertEqual(expected_object_name, "EUR")
