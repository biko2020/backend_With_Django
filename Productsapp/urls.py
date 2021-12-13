from django.conf.urls import url
from Productsapp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^categorie$',views.categorieApi),
    url(r'^categorie/([0-9]+)$',views.categorieApi),

    url(r'^producte$',views.productApi),
    url(r'^producte/([0-9]+)$',views.productApi),

    url(r'^producte/saveImage',views.SaveFile),
    url(r'^producte/(?P<getSelectCatory>[\w|\W]+)$',views.FilterCategorie),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

""" ([0-9]+)$  ?P<>[\w|\W] pour gérer le alphanumerique ainsi caracteres speciaux %"""