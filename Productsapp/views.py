
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Productsapp.models import Categories,Products
from Productsapp.serializers import CategoriesSerializer,ProductsSerializer

from django.core.files.storage import FileSystemStorage, default_storage

        # ************ ----- Categories 

@csrf_exempt
def categorieApi(request,id=0):
    if request.method=='GET':
        categories = Categories.objects.all()
        categories_serializer=CategoriesSerializer(categories, many=True)
        return JsonResponse(categories_serializer.data, safe=False)

    elif request.method=='POST':
        categorie_data=JSONParser().parse(request)
        categories_serializer=CategoriesSerializer(data=categorie_data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return JsonResponse("Enregistrer les données avec succès",safe=False)
        return JsonResponse("Erreur dans l'enregistrement des données..!",safe=False)
        
    elif request.method=='PUT':
        categorie_data=JSONParser().parse(request)
        categorie=Categories.objects.get(CategorieId=categorie_data['CategorieId'])

        categories_serializer=CategoriesSerializer(categorie,data=categorie_data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return JsonResponse("Méttre à jour les données avec succés",safe=False)
        return JsonResponse("Erreur de méttre à jour les données ..!")


    elif request.method=='DELETE':
        categorie=Categories.objects.get(CategorieId=id)
        categorie.delete()
        return JsonResponse("Suppressions des données avec succés",safe=False)

        # ************ ----- Products 

@csrf_exempt
def productApi(request,id=0):
    if request.method=='GET':
        producte = Products.objects.all()
        products_serializer=ProductsSerializer(producte,many=True)
        return JsonResponse(products_serializer.data,safe=False)

    elif request.method=='POST':
        product_data=JSONParser().parse(request)
        products_serializer=ProductsSerializer(data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Enregistrer les données avec succès",safe=False)
        return JsonResponse("Erreur dans l'enregistrement des données..!",safe=False)

    elif request.method=='PUT':
        product_data=JSONParser().parse(request)
        product=Products.objects.get(ProductId=product_data['ProductId'])
        products_serializer=ProductsSerializer(product,data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Méttre à jour les données avec succés",safe=False)
        return JsonResponse("Erreur de méttre à jour les données ..!")

    elif request.method=='DELETE':
        product=Products.objects.get(ProductId=id)
        # -- *** supprimer les images depuis le repertoir Media (/Photos) *** --
        file = FileSystemStorage()
        file.delete(product.PhotoFileName)
        product.delete()
        return JsonResponse("Suppressions des données avec succés", safe=False)
     
                            
#  *--- filter par categories ---*
@csrf_exempt

def FilterCategorie(request, getSelectCatory):
    if request.method == 'GET':
       categorie=Products.objects.filter(RefCategorie=getSelectCatory)
       categorie_serializer = ProductsSerializer(categorie,many=True) 
       return JsonResponse(categorie_serializer.data, safe=False)


# *---fonction sauvgarder le fichier un le repertoire photo
@csrf_exempt

def SaveFile(request):
    #if request.method == 'POST':
       Ourfile = request.FILES['uploadFile']
       Ourfile_name = default_storage.save(Ourfile.name, Ourfile)
       print("le nom du fichier :" ,Ourfile.name)
       print("la taille du fichier:" ,Ourfile.size)
       return JsonResponse(Ourfile_name, safe=False)   
    #return render(request,'uploadFile')


    






