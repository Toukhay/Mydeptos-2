from django.shortcuts import render


# Create your views here.
def post_property(request):
    return render(request, 'post_property')

def view_property(request):
    return render(request, 'view_property')