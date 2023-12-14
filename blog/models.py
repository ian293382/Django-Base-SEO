from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to='images')
    intro = models.TextField()
    body = models.TextField()

    class  Meta:
        ordering = ('-id',)

    def get_absolute_url(self):
        return self.slug