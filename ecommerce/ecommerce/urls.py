from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core.views import frontpage, about
from django.views.generic.base import TemplateView

urlpatterns = [
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('robot.txt', TemplateView.as_view(template_name='robot.txt', content_type='text/plain')),
    path('', include('userprofile.urls')), 
    path('', include('store.urls')),
    path('', frontpage, name='frontpage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
