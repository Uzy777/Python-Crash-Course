from django.db import models

# Create your models here.
class Pizza(models.Model):
    """Select a Pizza"""

    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model Pizza."""
        return self.name


class Topping(models.Model):
    """Select a Topping for the Pizza"""

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "toppings"

    def __str__(self):
        """Return a string representation of the model Topping."""
        return self.name