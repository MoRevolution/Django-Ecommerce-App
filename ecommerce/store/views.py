from django.db.models import Q 
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from .cart import Cart
from .forms import OrderForm
from .models import Product, Category, Order, OrderItem


def add_to_cart(request, product_id:str): 
    cart = Cart(request)
    cart.add(product_id=product_id)

    return redirect('cart_view')

def change_quantity(request, product_id:str):
    action = request.GET.get('action', None)
    cart = Cart(request)

    if action: 
        quantity = 1 

        if action == 'decrease':
            quantity = -1
        
        cart.add(product_id=product_id, quantity=quantity, update_quantity=True)

    return redirect('cart_view')

def cart_view(request): 
    cart = Cart(request)


    return render(request, 'store/cart_view.html', {
        'cart': cart,
    })

@login_required
def checkout(request): 
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            total_cost = 0
        
            for item in cart: 
                total_cost += item['product'].price * int(item['quantity'])

            order = form.save(commit=False)
            order.created_by = request.user
            order.paid_amount = total_cost
            order.save()

            for item in cart:
                item = OrderItem.objects.create(order = order,
                                                 product= item['product'], 
                                                 price = item['product'].price * int(item['quantity']), 
                                                 quantity = int(item['quantity']))
            
            cart.clear()

            return redirect('myaccount')
    else: 
        form = OrderForm()

    return render(request, 'store/checkout.html', {     
        'cart': cart,
        'form': form,
    })



def remove_from_cart(request, product_id: str):
    cart = Cart(request)
    cart.remove(product_id= product_id)

    return redirect('cart_view')

def search(request): 
    query = request.GET.get('query', '')
    products = Product.objects.filter(status = Product.ACTIVE).filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )

    return render (request, 'store/search.html', {
        'query':  query,
        'products': products,
    })

def category_detail(request, slug): 
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status = Product.ACTIVE)

    return render(request, 'store/category_detail.html', {
        'category': category, 
        'products': products,
    })
                   

def product_detail(request, category_slug, slug) : 
    product = get_object_or_404(Product, slug=slug, status = Product.ACTIVE)
    cart = Cart(request)
    
    print(cart.get_total_cost())
    return render(request, 'store/product_detail.html', {
        'product': product,
    })


