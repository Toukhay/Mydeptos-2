from django.shortcuts import render

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
    return render(request, 'listings.html', context)


def search(request):
    return render(request, 'search.html')

def view_property(request):
    return render(request, 'view_property.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def user_panel(request):
    return render(request, 'user_panel.html')

def post_property(request):
    return render(request, 'post_property.html')

def view_property(request):
    return render(request, 'view_property.html')

def favorites(request):
    return render(request, 'favorite.html')