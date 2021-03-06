from django.test import TestCase
from django.http import response
from django.urls import reverse

# Create your tests here.
class SnacksTest(TestCase):

    def test_snack_list_status(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    
    def test_snack_list_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response, 'snack_list.html')
    

    def test_snack_list_base_template(self):
        url = reverse('base')
        response = self.client.get(url)
        self.assertEqual(response, 'base.html')


    def test_snack_list_status(self):
        url = reverse('snack_detail')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    
    def test_snack_list_template(self):
        url = reverse('snack_detail')
        response = self.client.get(url)
        self.assertEqual(response, 'snack_detail.html')