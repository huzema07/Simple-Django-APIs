from django.db import models
from django.core.validators import MinValueValidator

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=30)
    pizza_name = models.CharField(max_length=25)
    flavour = models.CharField(max_length=25)

    size = models.CharField(max_length=10, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], default='M')

    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.00)])

    def __str__(self):
        return f"{self.brand_name} - {self.pizza_name} ({self.size})" 

