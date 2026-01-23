from django.db import models


class Hero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='hero/', null=True, blank=True)
    cta_text = models.CharField(max_length=50, default='View Packages')
    cta_link = models.CharField(max_length=200, default='/packages/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Hero Sections'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
