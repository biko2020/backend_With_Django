from django.db import models

# Create your models here.

""" -- -- Table Categories --- ----"""

class Categories(models.Model):
    CategorieId = models.AutoField(primary_key=True)
    CategorieName = models.CharField(max_length=500)

def __str__(self):
    return self.CategorieName

""" -- -- Table Produits --- ----"""
class Products(models.Model):
    
    ProductId = models.AutoField(primary_key=True)
    RefCategorie = models.CharField(max_length=500)
    ProductName = models.CharField(max_length=500)
    ProductDecrip = models.CharField(max_length=800)
    PhotoFileName = models.CharField(max_length=500)
    
def __str__(self):
    return self.RefCategorie
   
""" -- -- Table Slide page d'accueil --- ----"""
class Slide(models.Model):

    SlideId = models.AutoField(primary_key=True)
    SlideTitre = models.CharField(max_length=200)
    SlideDescription = models.CharField(max_length=600)
    SlidePhoto = models.CharField(max_length=200)

def __str__(self):
    return self.SlideTitre    

""" -- -- Table Partenaires --- ----"""
class Partenaires(models.Model):
    PartenaireId = models.AutoField(primary_key=True)
    PartenaireName = models.CharField(max_length=500)
    PartenaireLogo = models.CharField(max_length=200)

def __str__(self):
    return self.PartenaireName

""" -- -- Table Fournisseurs --- ----"""
class Fournisseur(models.Model):
    FournisseurId = models.AutoField(primary_key=True)
    FournisseurName = models.CharField(max_length=500)  
    FournisseurLogo = models.CharField(max_length=200)  

def __str__(self):
    return self.FournisseurName    


""" -- -- Table Formulaire d inscription --- ----"""

