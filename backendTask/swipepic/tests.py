from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Profile

class SwipePicViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='testpassword')
        self.profile = Profile.objects.create(
            user=self.user, phone_no='1234567890', otp='1234')

    def test_swipeimages_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('swipepic:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_history_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('swipepic:history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'history.html')