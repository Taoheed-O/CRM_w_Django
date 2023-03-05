from django.test import TestCase
from django.shortcuts import reverse
# Create your tests here.


class LandingPageTest(TestCase):
    def test_response(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

