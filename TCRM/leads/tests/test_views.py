from django.test import TestCase
from django.shortcuts import reverse
# Create your tests here.


class LandingPageTest(TestCase):
    def response_test(self):
        response = self.client.get(reverse("homepage"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "leads/homepage.html")
