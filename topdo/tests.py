from django.test import TestCase


class AppTestCase(TestCase):

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        self.assertEqual(1, 0)