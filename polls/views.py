from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render


from .models import Product
from .models import Client
from .models import Employee


def index(request):
    latest_product_list = Product.objects.all()
    template = loader.get_template('index.html')
    context = {
        'latest_product_list': latest_product_list,
    }
    return HttpResponse(template.render(context, request))

def cl(request):
    latest_clients_list = Client.objects.all()
    template = loader.get_template('clients.html')
    context = {
        'latest_clients_list': latest_clients_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', {'product': product})

def detail_cl(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'detail_cl.html', {'client': client})

