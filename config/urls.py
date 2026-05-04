from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Wonderlander Wellness - ადმინ პანელი"
admin.site.site_title = "Wonderlander Admin"
admin.site.index_title = "მართვის პანელი"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
