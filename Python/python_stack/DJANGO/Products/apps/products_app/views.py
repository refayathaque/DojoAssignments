from django.shortcuts import render, HttpResponse, redirect

from .models import Product
def index(request):
    Product.objects.create(name= 'Audi A4', description= 'The sensible but uninspiring choice')
    Product.objects.create(name= 'Jaguar XE', description= 'The exhilirating but financially foolish choice')
    Product.objects.create(name= 'BMW 3-Series', description= 'The perfect blend of athleticism and craftsmanship')
    product = Product.objects.all()
    print product
    for i in product: # i is variable used to iterate through table 'Product'
        print i.name, i.description # prints name and description inside each dictionary within QuerySet
    return render(request, 'products_app/index.html')
