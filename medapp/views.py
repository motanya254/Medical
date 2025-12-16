from django.shortcuts import render, get_object_or_404
from .models import Facility


# --------------------------
# STATIC PAGES
# --------------------------
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


# --------------------------
# FACILITY LIST (Search + Filters)
# --------------------------
def facilityl(request):
    facilities = Facility.objects.all()

    # Search by name
    q = request.GET.get('q')
    if q:
        facilities = facilities.filter(name__icontains=q)

    # Type filter
    f_type = request.GET.get('type')
    if f_type:
        facilities = facilities.filter(facility_type=f_type)

    # Level filter
    level = request.GET.get('level')
    if level:
        facilities = facilities.filter(level=level)

    return render(request, 'facilityl.html', {'facilities': facilities})


# --------------------------
# FACILITY DETAIL PAGE
# --------------------------
def facilityd(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    return render(request, 'facilityd.html', {'facility': facility})


# --------------------------
# SEARCH PAGE
# --------------------------
def searchfacility(request):
    facilities = Facility.objects.all()

    q = request.GET.get('q')
    if q:
        facilities = facilities.filter(name__icontains=q)

    return render(request, 'searchfacility.html', {'facilities': facilities})
