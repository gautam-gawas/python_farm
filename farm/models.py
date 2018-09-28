from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Farmer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=True, null=True)
    language = models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return self.name


class Farm(models.Model):
    farmer = models.ForeignKey('Farmer',on_delete=models.CASCADE,)
    area = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    crop_grown = models.CharField(max_length=50,blank=True, null=True)
    sowing_date  = models.DateField(blank=True, null=True)

    def __str__(self):
        return (self.farmer.name + " - " + self.village)

class Schedule(models.Model):
    UNIT_CHOICES = (
        ('1', 'Ton'),
        ('2', 'Kilo-gram'),
        ('3', 'gram'),
        ('4', 'mili-litre'),
        ('5', 'litre'),
    )

    farm = models.ForeignKey('Farm', on_delete=models.CASCADE, )
    fertiliser = models.CharField(max_length=100,blank=True, null=True)
    days_after_sowing = models.PositiveIntegerField(blank=True, null=True)
    quantity_unit = models.CharField(max_length=10, choices=UNIT_CHOICES,blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return (self.farm.farmer.name + " - " + self.fertiliser)


