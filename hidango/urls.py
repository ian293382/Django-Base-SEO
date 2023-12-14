from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from django.contrib.sitemaps.views import sitemap
from .sitemaps import SaticViewSitemap, PostViewSitemap

sitemaps = {'static': SaticViewSitemap , 'posts': PostViewSitemap }
urlpatterns = [
    path("robot.txt", TemplateView.as_view(template_name='core/robot.txt', content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('',include('blog.urls')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


