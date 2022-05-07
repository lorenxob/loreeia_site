from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.
class Machines(models.Model):
    machine_name=models.CharField(max_length=250)
    buy_date=models.DateField("Fecha de compra", auto_now_add=True)
    marca=models.CharField(max_length=250)

class Devices(models.Model):
    machines= models.ForeignKey(Machines, on_delete=SET_NULL, null=True)
    device_name=models.CharField(max_length=250)
    secret=models.CharField(max_length=250)
