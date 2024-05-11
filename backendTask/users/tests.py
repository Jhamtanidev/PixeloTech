from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile

class UserViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='testpassword')
        self.profile = Profile.objects.create(
            user=self.user, phone_no='+919638570210', otp='1234')

    def test_register_view(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
    def test_login_view(self):
        response = self.client.post(reverse('users:login'), {'mobile': self.profile.phone_no})
        self.assertEqual(response.status_code, 302)  # Check for a 302 (Found) status code
        response = self.client.post(reverse('users:otp'))

    def test_otp_view(self):
        self.client.login(first_name='testuser', password='testpassword')
        session = self.client.session
        session['phone_no'] = self.profile.phone_no
        session.save()

        response = self.client.post(reverse('users:otp'), {'otp': self.profile.otp})
        self.assertEqual(response.status_code, 302)
        

def test_registration_flow(self):
    # Register a new user
    response = self.client.post(reverse('users:register'), {
        'email': 'newuser@example.com',
        'mobile': '+919638570210',
    })
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('users:otp'))

    # Verify the OTP
    user = User.objects.get(email='newuser@example.com')
    profile = Profile.objects.get(user=user)
    response = self.client.post(reverse('users:otp'), {
        'otp': profile.otp,
        'mobile': profile.phone_no,
    })
    self.assertEqual(response.status_code, 302)
   

    # Set the username
   
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('swipepic:dashboard'))
    user.refresh_from_db()
    self.assertEqual(user.first_name, 'New User')

def test_login_flow(self):
    # Login with a registered user
    response = self.client.post(reverse('users:login'), {
        'mobile': self.profile.phone_no,
    })
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('users:otp'))

    # Verify the OTP
    response = self.client.post(reverse('users:otp'), {
        'otp': self.profile.otp,
        'mobile': self.profile.phone_no,
    })
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('swipepic:dashboard'))        