"""fabrique_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from fabrique_test import settings
from django.conf.urls import url
from django.views.generic import RedirectView
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(f'{settings.PROJECT_NAME}.apps.api.urls')),
]

urlpatterns += [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),

    path('openapi/', get_schema_view(
        title="School Service",
        description="API developers hoping to use our service"
    ), name='openapi-schema'),
    path('docs/',
         TemplateView.as_view(extra_context={'schema_url': 'openapi-schema'}, template_name='docs/swagger-ui.html'),
         name='swagger-ui'),

]

if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
