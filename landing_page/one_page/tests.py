from django.test import TestCase
from django.urls import reverse

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
class ContactViewTest(TestCase):
    """check the email form with some cases"""
    valid_data = "test1@test.com"
    
    def test_email_form(self):
        """email is valid"""
        response = self.client.post(reverse('one_page:home_page'), {'email': self.valid_data})
        self.assertTrue(response.context['form'].is_valid())
        
        response.context['form'].save()
        self.assertTrue(ContactDatabase.objects.filter(email=self.valid_data).exists())

        