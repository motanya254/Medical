from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Facility, Service
from django.db import models
from .forms import ContactForm


# --------------------------
# STATIC PAGES
# --------------------------
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    """Render contact page and process submitted contact form.

    When the form is posted and valid we save the message and display a
    success alert. Errors are shown inline via the form object.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # attempt to notify administrators via email if configured
            try:
                contact.send_notification()
            except Exception:
                # don't block the user for email backend problems
                pass
            messages.success(request, "Thank you for your message. We'll be in touch soon!")
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # respond with JSON for client-side scripts
                from django.http import JsonResponse
                return JsonResponse({'status': 'ok', 'message': 'saved'})
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


# --------------------------
# FACILITY LIST (Search + Filters)
# --------------------------
def facilityl(request):
    # always load related services to avoid N+1
    facilities = Facility.objects.all().prefetch_related('services')
    services_list = Service.objects.all()

    # general search (name, location, type, opening hours or service)
    q = request.GET.get('q')
    if q:
        facilities = facilities.filter(
            models.Q(name__icontains=q) |
            models.Q(location__icontains=q) |
            models.Q(facility_type__icontains=q) |
            models.Q(opening_hours__icontains=q) |
            models.Q(services__name__icontains=q)
        ).distinct()

    # service filter (by name or id)
    svc = request.GET.get('service')
    if svc:
        facilities = facilities.filter(services__name__icontains=svc)

    # minimum rating
    rating = request.GET.get('rating')
    if rating:
        try:
            r = float(rating)
            facilities = facilities.filter(rating__gte=r)
        except ValueError:
            pass

    # type filter
    f_type = request.GET.get('type')
    if f_type:
        facilities = facilities.filter(facility_type=f_type)

    # level filter
    level = request.GET.get('level')
    if level:
        facilities = facilities.filter(level=level)

    # opening hours substring
    opening = request.GET.get('opening_hours')
    if opening:
        facilities = facilities.filter(opening_hours__icontains=opening)

    context = {
        'facilities': facilities,
        'services_list': services_list,
    }
    return render(request, 'facilityl.html', context)


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
    facilities = Facility.objects.all().prefetch_related('services')
    services_list = Service.objects.all()

    q = request.GET.get('q')
    if q:
        facilities = facilities.filter(
            models.Q(name__icontains=q) |
            models.Q(location__icontains=q) |
            models.Q(facility_type__icontains=q) |
            models.Q(opening_hours__icontains=q) |
            models.Q(services__name__icontains=q)
        ).distinct()

    svc = request.GET.get('service')
    if svc:
        facilities = facilities.filter(services__name__icontains=svc)

    rating = request.GET.get('rating')
    if rating:
        try:
            r = float(rating)
            facilities = facilities.filter(rating__gte=r)
        except ValueError:
            pass

    f_type = request.GET.get('type')
    if f_type:
        facilities = facilities.filter(facility_type=f_type)

    opening = request.GET.get('opening_hours')
    if opening:
        facilities = facilities.filter(opening_hours__icontains=opening)

    return render(request, 'searchfacility.html', {
        'facilities': facilities,
        'services_list': services_list,
    })
