from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Facility, Service


# --------------------
# SERVICE ADMIN (manual entry OK)
# --------------------
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# --------------------
# FACILITY RESOURCE
# --------------------
class FacilityResource(resources.ModelResource):
    class Meta:
        model = Facility
        fields = (
            'name',
            'location',
            'facility_type',
            'level',
            'description',
            'phone',
            'email',
            'opening_hours',
            'has_emergency',
            'rating',
        )


# --------------------
# FACILITY ADMIN
# --------------------
@admin.register(Facility)
class FacilityAdmin(ImportExportModelAdmin):
    resource_class = FacilityResource

    list_display = ("name", "facility_type", "level", "has_emergency")
    list_filter = ("facility_type", "level", "has_emergency")
    search_fields = ("name", "location")

    filter_horizontal = ("services",)
