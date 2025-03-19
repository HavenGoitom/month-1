from django.db import models

# Create your models here.
class Loans(models.Model):
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    is_paid =models.BooleanField(default= False)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title