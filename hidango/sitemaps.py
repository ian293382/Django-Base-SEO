from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from django.shortcuts import reverse

from blog.models import Post

class SaticViewSitemap(Sitemap):
    def items(self):
        return ['core:index', 'core:about',]
    
    def location(self, item):
        return reverse(item)
    
class PostViewSitemap(Sitemap):
    def items(self):
        return Post.objects.all()
             