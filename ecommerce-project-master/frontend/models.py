from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('T', 'Top'),
    ('B', 'Bottom'),
    ('S', 'Shoes')
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title