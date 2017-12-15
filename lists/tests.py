from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

	def test_home_page_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

	def test_can_save_a_POST_request(self):
		text = 'A new list item'
		response = self.client.post('/', data={'item_text': text})
		self.assertIn(text, response.content.decode())
		self.assertTemplateUsed(response, 'home.html')

	