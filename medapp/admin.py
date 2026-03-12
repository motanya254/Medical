from django.contrib import admin
from .models import Facility, Service, ContactMessage


# --------------------
# SERVICE ADMIN
# --------------------
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# --------------------
# CONTACT MESSAGE ADMIN
# --------------------
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "sent_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("sent_at",)


# --------------------
# FACILITY ADMIN
# --------------------
@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ("name", "facility_type", "level", "has_emergency")
    list_filter = ("facility_type", "level", "has_emergency")
    search_fields = ("name", "location")
    filter_horizontal = ("services",)
