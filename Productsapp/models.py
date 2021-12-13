from django.db import models

# Create your models here.
class Categories(models.Model):
    CategorieId = models.AutoField(primary_key=True)
    CategorieName = models.CharField(max_length=500)

def __str__(self):
    return self.CategorieName

class Products(models.Model):
    
    ProductId = models.AutoField(primary_key=True)
    RefCategorie = models.CharField(max_length=500)
    ProductName = models.CharField(max_length=500)
    ProductDecrip = models.CharField(max_length=500)
    PhotoFileName = models.CharField(max_length=500)
    
def __str__(self):
    return self.RefCategorie
   