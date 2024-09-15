from django.db import models


class Laptop(models.Model):
    BRAND_CHOICES = [
        ('apple', 'Apple'),
        ('dell', 'Dell'),
        ('hp', 'HP'),
        ('lenovo', 'Lenovo'),
        ('asus', 'Asus'),
    ]

    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    model = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    ram_size = models.PositiveIntegerField()
    storage_size = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f'{self.brand} {self.model}'


class LaptopPhoto(models.Model):
    laptop = models.ForeignKey(Laptop, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='laptop_photos/')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Photo of {self.laptop}'
