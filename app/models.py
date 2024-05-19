from django.db import models

# Create your models here.
class Fruits(models.Model):
    fruit_name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images')
    scientific_name=models.CharField(max_length=100)
    cost=models.CharField(max_length=5,blank=True)
    def __str__(self):
        return self.fruit_name
    
