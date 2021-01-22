from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from .forms import ProductForm #, RawProductForm
from .models import Product
# Create your views here.

#Created views for each of the CRUD actions
#Using Django login_required to only allow logged in users to access inventory
#If an unauthenticated user tries to access our inventory, we redirect them to our login page

@login_required(login_url='/login/')
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

@login_required(login_url='/login/')
def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

@login_required(login_url='/login/')
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

@login_required(login_url='/login/')
def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

@login_required(login_url='/login/')
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)