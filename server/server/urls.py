from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dealership.urls')),
    path('about/', TemplateView.as_view(template_name='About.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='Contact.html'), name='contact'),
    # Serve React index.html for all other routes
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]