from django.shortcuts import render

# Create your views here.
def favorite(request):
    return render(request, 'favorite.html')
def listings(request):
    return render(request, 'listings.html')
def search(request):
    return render(request, 'search.html')