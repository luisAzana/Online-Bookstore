# Django

from django.contrib import admin

from django.urls import path
from django.urls import include

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView


urlpatterns = [

    path(
        route = 'admin/', 
        view = admin.site.urls
    ),
    
    path(
        route = 'catalog/', 
        view = include('catalog.urls')
    ),    

    # Add URL maps to redirect the base URL to our application
    path(
        route = '', 
        view = RedirectView.as_view(url='/catalog/', permanent=True)
    ),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]