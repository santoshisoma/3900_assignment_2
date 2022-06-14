from django.urls import include, re_path
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]




