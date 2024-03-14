from django.shortcuts import render
from .models import Listing

def home(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        property_type = request.POST.get('property_type')
        bedrooms = request.POST.get('bedrooms')
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')

        listings = Listing.objects.filter(
            city__icontains=location,
            property_type__iexact=property_type,
            num_bedrooms__gte=bedrooms,
            price__gte=min_price,
            price__lte=max_price,
        )

        context = {'listings': listings}
        return render(request, 'home.html', context)

    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def listings(request):
    listings = Listing.objects.all()
    context = {'listings': listings}
    return render(request, 'listings/templates/listings.html', context)

def login(request):
    return render(request, 'usuarios/login.html')

def register(request):
    return render(request, 'usuarios/register.html')

def search(request):
    return render(request, 'listings/templates/search.html')

def view_property(request):
    return render(request, 'property/templates/view_property.html')

def user_panel(request):
    return render(request, 'accounts/templates/user_panel.html')