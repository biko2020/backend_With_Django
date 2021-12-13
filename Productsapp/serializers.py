from rest_framework import serializers
from Productsapp.models import Categories,Products

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categories 
        fields=('CategorieId','CategorieName')

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products 
        fields=('ProductId','RefCategorie','ProductName','ProductDecrip','PhotoFileName')