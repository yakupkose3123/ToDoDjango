from django.test import TestCase
from .forms import ToDoForm

class UnitTestCase(TestCase):
    
    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'app/home.html')

