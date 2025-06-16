from django.shortcuts import render, redirect
from .models import Product, Commande
from django.core.paginator import Paginator

def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')

    if item_name != '' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)

    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_object': product_object})

def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        tel = request.POST.get('tel')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')

        if pays == "autre":
            pays = request.POST.get("autre_pays")

        com = Commande(
            items=items,
            total=total,
            nom=nom,
            email=email,
            address=address,
            ville=ville,
            pays=pays,
            zipcode=zipcode,
            tel=tel
        )
        com.save()
        return redirect('confirmation')  # ← IMPORTANT

    return render(request, 'shop/checkout.html')

def confirmation(request):
    info = Commande.objects.last()
    nom = info.nom if info else "Client"
    return render(request, 'shop/confirmation.html', {'name': nom})
