from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('events.html', views.events, name='events'),
    path('single.html', views.events, name='page'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)