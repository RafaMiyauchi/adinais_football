import datetime
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
from main.forms import ProductForm
from main.models import Product

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        products_list = Product.objects.all()
    else:
        products_list = Product.objects.filter(user=request.user)
    
    context = {
        'app_name': 'Adinais Football',
        'name': request.user.username,
        'class': 'PBD KKI',
        'products': products_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

# --- Standard Sync Views (kept as fallbacks) ---
@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        messages.success(request, "Product added successfully!")
        return redirect('main:show_main')
    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == "POST":
        form.save()
        messages.success(request, f"'{product.name}' updated successfully!")
        return redirect('main:show_detail', id=id)
    context = {'form': form, 'product': product}
    return render(request, "edit_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        product.delete()
        messages.success(request, f"'{product.name}' has been deleted.")
    return redirect('main:show_main')


# AJAX Sections
@csrf_exempt
def add_product_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({"status": "error", "message": "Authentication required."}, status=401)
    
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            # Sanitize inputs
            product.name = strip_tags(product.name)
            product.description = strip_tags(product.description)
            product.save()
            return JsonResponse({"status": "success", "message": "Product added successfully!"}, status=201)
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

@csrf_exempt
def edit_product_ajax(request, id):
    if not request.user.is_authenticated:
        return JsonResponse({"status": "error", "message": "Authentication required."}, status=401)
    
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            updated_product = form.save(commit=False)
            updated_product.name = strip_tags(updated_product.name)
            updated_product.description = strip_tags(updated_product.description)
            updated_product.save()
            return JsonResponse({"status": "success", "message": "Product updated successfully."})
        else:
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

@csrf_exempt
def delete_product_ajax(request, id):
    if not request.user.is_authenticated:
        return JsonResponse({"status": "error", "message": "Authentication required."}, status=401)

    if request.method == "POST":
        try:
            product = Product.objects.get(pk=id)
            product.delete()
            return JsonResponse({"status": "success", "message": "Product deleted successfully."})
        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Product not found."}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=405)

def get_product_json(request, id):
    product = get_object_or_404(Product, pk=id)
    data = {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "thumbnail": product.thumbnail,
        "category": product.category,
        "stock": product.stock,
        "brand": product.brand,
        "rating": product.rating,
    }
    return JsonResponse(data)

def show_json(request):
    user = request.user
    if user.is_authenticated:
        products = Product.objects.filter(user=user)
    else:
        products = Product.objects.all()
        
    data = []
    for item in products:
        data.append({
            "id": item.id,
            "user_id": item.user.id if item.user else None,
            "name": item.name,
            "price": item.price,
            "description": item.description,
            "thumbnail": item.thumbnail,
            "category": item.category,
            "stock": item.stock,
            "brand": item.brand,
            "rating": item.rating,
        })
    return JsonResponse(data, safe=False)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Registration successful! You can now log in.'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)

@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response_data = {'status': 'success', 'message': 'Login successful!'}
            response = JsonResponse(response_data)
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid username or password.'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)

def register(request):
    form = UserCreationForm()
    return render(request, "register.html", {'form': form})

def login_user(request):
    form = AuthenticationForm()
    return render(request, "login.html", {'form': form})

@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response