# Bismillahirahmanirahim
from django.shortcuts import render, get_object_or_404,redirect
from .models import Product
from .forms import ProductForm
# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'gallery/product_list.html', {'products': products})

def product_detail(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'gallery/product_detail.html', {'product': product})

def edit_product(request,pk):
    product = get_object_or_404(Product,pk=pk)
    if request.method == 'POST':
        # instance variable needs to be given if we need to save it in place of the previous entry
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request,'gallery/edit.html',{
        'form':form,
        'title':product.name
        })

def delete_product(request,pk):
    product = get_object_or_404(Product, pk= pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request,'gallery/delete.html',{'product':product})