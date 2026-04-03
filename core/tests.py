from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Enquiry, Coach, GalleryImage

class RockstarModelTests(TestCase):
    def test_enquiry_creation(self):
        enquiry = Enquiry.objects.create(
            name="John Doe",
            email="john@example.com",
            mobile_number="1234567890"
        )
        self.assertEqual(enquiry.name, "John Doe")
        self.assertTrue(Enquiry.objects.exists())

    def test_coach_creation(self):
        coach = Coach.objects.create(
            name="Coach Alex",
            specialty="Freestyle",
            experience="10 years"
        )
        self.assertEqual(str(coach), "Coach Alex")

    def test_gallery_image_creation(self):
        img = GalleryImage.objects.create(
            title="Pool View",
            image_url="https://example.com/pool.jpg"
        )
        self.assertEqual(img.title, "Pool View")

class RockstarViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            username='admin', 
            password='password123', 
            email='admin@test.com'
        )
        self.regular_user = User.objects.create_user(
            username='guest', 
            password='password123'
        )

    def test_homepage_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_gallery_loads(self):
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)

    def test_coaches_loads(self):
        response = self.client.get(reverse('coaches'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_access_denied_to_guest(self):
        # Should redirect to login
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_access_allowed_to_admin(self):
        self.client.login(username='admin', password='password123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_enquiry_submission(self):
        response = self.client.post(reverse('home'), {
            'name': 'Tester',
            'email': 'test@test.com',
            'mobile_number': '9999999999'
        })
        self.assertEqual(response.status_code, 302) # Redirects after success
        self.assertTrue(Enquiry.objects.filter(name='Tester').exists())
