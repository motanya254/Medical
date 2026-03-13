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
# Contact message (from contact form)
# --------------------------
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} <{self.email}> - {self.subject}"

    def send_notification(self, recipient_list=None):
        """Send an email copy of this message to the given recipients.

        By default the message is mailed to the site administrators defined in
        ``settings.ADMINS``.  This helper makes it easy to plug-in an SMTP
        backend and keeps the view logic minimal.
        """
        from django.core.mail import send_mail
        from django.conf import settings

        if recipient_list is None:
            # fall back to settings, expecting a list of (name, email) tuples
            recipient_list = [email for _, email in getattr(settings, 'ADMINS', [])]


        if not recipient_list:
            # nothing to send to
            return

        send_mail(
            subject=self.subject,
            message=self.message,
            from_email=self.email,
            recipient_list=recipient_list,
            fail_silently=True,
        )


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

    @property
    def formatted_opening_hours(self):
        """Return opening hours in 12‑hour format with AM/PM if parseable.

        The raw data is stored as text (for example "0800-1700" or "08:00-17:00").
        This helper attempts to convert it to something like "8:00 AM – 5:00 PM".
        If the string can't be parsed it is returned unchanged.
        """
        if not self.opening_hours:
            return ""
        import re
        from datetime import datetime

        # split on dash with optional spaces
        parts = re.split(r"\s*-\s*", self.opening_hours.strip())
        formatted = []
        for p in parts:
            # try several common patterns
            for fmt in ("%H%M", "%H:%M", "%I:%M%p", "%I:%M %p"):
                try:
                    dt = datetime.strptime(p, fmt)
                    formatted.append(dt.strftime("%I:%M %p").lstrip("0"))
                    break
                except ValueError:
                    continue
            else:
                # nothing matched; keep raw
                formatted.append(p)
        return " – ".join(formatted)

    def __str__(self):
        return self.name
