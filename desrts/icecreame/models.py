from django.db import models

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=30,default="")
    price=models.IntegerField(default=100)
    flavour=models.CharField(max_length=10)



    def __str__(self):
        return self.name
