from django.http import JsonResponse
from .models import Product,Menu

def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())}
    response = JsonResponse(data)
    return response

def product_detail(request,pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
                  "name": product.name,
                #   "menu": product.menu,
                  "description": product.description,
                  "photo": product.photo.url,
                  "price": product.price,
                  "shipping_cost": product.shipping_cost,
                  "quantity": product.quantity,

                }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "product not found!"
          }},
           status=404)
    return response


def menu_list(request):
    menu = Menu.objects.filter(active=True)
    data = {"menu": list(menu.values())}
    response = JsonResponse(data)
    return response


def menu_detail(request,pk):
    try:
        menu = Menu.objects.get(pk=pk)
        menu_onlines = menu.onlines.all()
        data = {"menu": {
                  "name": menu.name,
                  "location": menu.location,
                  "active": menu.active,
                  "onlines": list(menu_onlines.values())
                  
                }}
        response = JsonResponse(data)
    except Menu.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "menu not found!"
          }},
           status=404)
    return response