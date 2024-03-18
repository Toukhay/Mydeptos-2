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
from django.urls import include, path
from django.conf.urls.static import static
from . import views
from django.conf import settings


from home import views as hviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hviews.homee, name='home'),
    path('about/', hviews.about, name='about'),
    path('contact/', hviews.contact, name='contact'),
    path('listings/', hviews.listings, name='listings'),
    path('usuarios/login', views.login_view, name='login'),
    path('register/', hviews.register, name='register'),
    path('search/', hviews.search, name='search'),
    path('view_property/', hviews.view_property, name='view_property'),
    path ('user_panel/', hviews.user_panel, name='user_panel'),
    path('post_property/', hviews.post_property,name='post_property'),
    path('view_property/', hviews.view_property, name='view_property'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)