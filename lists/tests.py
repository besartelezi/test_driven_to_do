from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        #* call self.client.get, passing it the URL we want to test
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        