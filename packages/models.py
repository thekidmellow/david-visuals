from django.db import models


class Package(models.Model):
    CATEGORY_CHOICES = [
        ('logo', 'Logo Design'),
        ('social', 'Social Media'),
        ('flyer', 'Flyer/Poster'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    features = models.TextField(help_text='Enter features separated by new lines')
    delivery_time = models.CharField(max_length=100, default='3-5 business days')
    revisions = models.IntegerField(default=2)
    image = models.ImageField(upload_to='packages/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'price']

    def __str__(self):
        return self.name

    def get_features_list(self):
        return self.features.split('\n')