from django.test import TestCase

from one_page.models import ContactDatabase


# Create your tests here.
class ContactDatabaseTest(TestCase):
    """Unit test for the application"""
    @classmethod
    def setUpTestData(cls):
        ContactDatabase.objects.create(email='test1@test.com')

    def test_email_max_length(self):
        """Test that email has a maximum length"""
        email = ContactDatabase.objects.get(id=1)
        max_length = email._meta.get_field('email').max_length
        self.assertEqual(max_length, 100)
        
    def check_non_repetable_email(self):
        """Check duplicate emails are not allowed"""
        ContactDatabase.objects.create(email='test1@test.com')
        self.assertRaises(ValidationError)
        