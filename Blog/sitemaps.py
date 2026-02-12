from django.contrib.sitemaps import Sitemap
from .models import Post
from django.urls import reverse


class SitemapPost(Sitemap):
    changefreq="daily"
    priority=0.8


    def items(self):
        return Post.objects.all()
    

    def location(self, obj):
        return reverse("post",args=[obj.id])