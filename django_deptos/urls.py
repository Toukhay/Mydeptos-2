"""
URL configuration for django_deptos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from home import views
from listings import views
from property import views
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('listings/', views.listings, name='listings'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path ('user_panel/', views.user_panel, name='user_panel'),
    path('post_property/', views.post_property,name='post_property'),
    path('view_property/', views.view_property, name='view_property'),
    path('favorites/', views.favorites, name='favorites'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)