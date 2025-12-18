from django.contrib import admin
from .models import Facility, Service


# --------------------
# SERVICE ADMIN
# --------------------
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# --------------------
# FACILITY ADMIN
# --------------------
@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ("name", "facility_type", "level", "has_emergency")
    list_filter = ("facility_type", "level", "has_emergency")
    search_fields = ("name", "location")
    filter_horizontal = ("services",)
