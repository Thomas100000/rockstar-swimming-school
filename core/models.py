from django.db import models
from django.core.validators import RegexValidator

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', 
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    mobile_number = models.CharField(validators=[mobile_regex], max_length=17)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name_plural = "Enquiries"

class Coach(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=200)
    experience = models.CharField(max_length=50)
    # Using a simple URL or CharField for now to avoid media config complexity, 
    # but could be ImageField in production.
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Coaches"

class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255) # Can point to static/img/
    category = models.CharField(max_length=50, default="General")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
