import unittest
from django.test import Client, TransactionTestCase
from django.contrib.auth import get_user_model

from . import models

# Create your tests here.

TEST_USER = {
    'username': 'caxthetyx',
    'password': 'bvQ7%rpxz2*4o2',
}

USER_AGENT = {
    'win': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'macOS': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'linux': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'custom': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
}

class ProfileTests(TransactionTestCase):
    """Testing the models"""
    def test_whether_user_profile_created_on_user_creation_signal(self):
        django_user_model = get_user_model().objects.create_user(
            TEST_USER['username'], TEST_USER['password']
        )
        custom_profile = models.Profile.objects.get(user=django_user_model)
        self.assertEqual(custom_profile.user, django_user_model)

class HttpTests(unittest.TestCase):
    """Testing HTTP results"""
    def test_user_registration(self):
        client = Client()
        response = client.post('/register/', {
            'username': TEST_USER['username'],
            'password1': TEST_USER['password'],
            'password2': TEST_USER['password'],
            }, HTTP_USER_AGENT=USER_AGENT['win'])
        self.assertEqual(response.status_code, 302)

    def test_user_login(self):
        client = Client()
        response = client.post('/login/', {
            'username': TEST_USER['username'],
            'password1': TEST_USER['password'],
            }, HTTP_USER_AGENT=USER_AGENT['win'])
        self.assertEqual(response.status_code, 200)
    
    def test_user_logout(self):
        client = Client()
        response = client.post('/logout/',
            HTTP_USER_AGENT=USER_AGENT['win'])
        self.assertEqual(response.status_code, 302)
        
    # questa non va 
    def test_user_page(self, request='GET'):
        client = Client()
        response = client.get(f'/profile/{models.Profile.objects.get(pk=request.user.id)}',
            HTTP_USER_AGENT=USER_AGENT['win'])
        self.assertEqual(response.status_code, 200)
        