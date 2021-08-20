"""khoa URL Configuration

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
from django.urls import path
from django.conf.urls import include
from event.views import multiple_forms
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.models import User, Group


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', multiple_forms),
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static (settings.MEDIA_URL,
                              document_root = settings.MEDIA_ROOT)


                              
admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = "Khoa tin DHSP Huế"
admin.site.site_title = "DHSP Huế"
admin.site.index_title = "CLB Tin học"
