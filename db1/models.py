from django.db import models
from django.forms import ModelForm

class Customer(models.Model):
    id=models.IntegerField(primary_key='id')
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name



class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields=['id','name']

# Create your models here.
