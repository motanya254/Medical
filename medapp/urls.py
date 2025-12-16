from django.urls import path
from medapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

    # Facility list page
    path('facilityl/', views.facilityl, name="facilityl"),

    # Facility detail dynamic page
    path('facility/<int:pk>/', views.facilityd, name="facilityd"),

    # Search page
    path('searchfacility/', views.searchfacility, name='searchfacility'),



]
