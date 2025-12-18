from django.db import models
from django.utils.text import slugify

# --------------------------
# Service Model
# --------------------------
class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# --------------------------
# Facility Model
# --------------------------
class Facility(models.Model):
    class Meta:
        verbose_name_plural = "Facilities"

    # Facility Types
    FACILITY_TYPES = [
        ("Hospital", "Hospital"),
        ("Health Centre", "Health Centre"),
        ("Dispensary", "Dispensary"),
        ("Clinic", "Clinic"),
        ("Pharmacy", "Pharmacy"),
        ("Laboratory", "Laboratory"),
        ("Maternity", "Maternity"),
    ]

    # Levels
    LEVELS = [
        ("2", "Level 2"),
        ("3", "Level 3"),
        ("4", "Level 4"),
        ("5", "Level 5"),
    ]

    # Core fields
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    location = models.CharField(max_length=200)
    facility_type = models.CharField(max_length=50, choices=FACILITY_TYPES)
    level = models.CharField(max_length=10, choices=LEVELS)
    description = models.TextField(blank=True, null=True)

    # Contact fields
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    opening_hours = models.CharField(max_length=200, blank=True, null=True)

    # Other info
    has_emergency = models.BooleanField(default=False)
    rating = models.FloatField(default=0)

    # Image (TEMPORARILY stored as text to avoid Pillow dependency)
    image = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Image filename or URL (ImageField disabled for portability)"
    )

    # Services
    services = models.ManyToManyField(Service, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Auto-generate slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # Get list of services as string
    def get_services_list(self):
        return ", ".join([s.name for s in self.services.all()])

    def __str__(self):
        return self.name
