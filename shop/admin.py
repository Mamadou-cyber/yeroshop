from django.contrib import admin
from .models import category , Product,Commande

# Register your models here.
admin.site.site_header = "E-commerce"
admin.site.site_title = "MYTshop"
admin.site.index_title= "manager"
class AdminCategorie(admin.ModelAdmin):
     list_display=('name','date_added')
     
class AdminProduct(admin.ModelAdmin):
     list_display =('title','price','category','date_added')
     search_fields =('title',)
     list_editable=('price',)
class AdminCommande(admin.ModelAdmin) :
     list_display= ('items','nom','email','address','tel','ville','pays','total','date_commande')
admin.site.register(Product ,AdminProduct)
admin.site.register(category ,AdminCategorie)
admin.site.register(Commande,AdminCommande)