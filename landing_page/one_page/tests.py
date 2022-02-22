from django.test import TestCase

from one_page.models import ContactDatabase
from one_page.forms import ContactForm



# Create your tests here.

# testing the models.py
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
        
    def test_email_label(self):
        """Test that email has a label"""
        email = ContactDatabase.objects.get(id=1)
        field_label = email._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')
        
# testing the forms.py
class ContactFormTest(TestCase):
    def test_contact_form_email_label(self):
        """Test that contact form has correct label"""
        form = ContactForm()
        self.assertTrue(form.fields['email'].label is None or
                        form.fields['email'].label == 'Please insert your email')
        
# testing the views.py
# see https://stackoverflow.com/questions/53531753/django-testing-in-creating-a-user-with-email-address-which-is-from-session-input