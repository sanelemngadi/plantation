from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from cart.models import PlantationCartModel, PlantationProductDetails
from products.models import PlantationProduct
from orders.forms import PlantationAddressForm, PlantationCardInformationForm, PlantationOrderForm

# Create your views here.
@login_required(login_url="/users/login/")
def cart_list_view(request):
    cart = PlantationCartModel.objects.filter(user = request.user).first()
    return render(request, "cart.html", { "cart": cart })


@login_required(login_url="/users/login/")
def add_to_cart_view(request, pk, path):
    product = get_object_or_404(PlantationProduct, pk = pk)

    cart = PlantationCartModel.objects.filter(user = request.user).first()

    if not cart:
        cart = PlantationCartModel.objects.create(user = request.user)
        cart.save()

    if not cart.items.filter(product = product).exists():
        print("product is availabel but: ", cart.items.all().first())
        cart_item, created = PlantationProductDetails.objects.get_or_create(product=product, defaults={'quantity': 1})
        cart.items.add(cart_item)
        cart.save()
    else:
        item = cart.items.filter(product = product).first()
        item.increment()
        cart.save()

    return redirect(path)


@login_required(login_url="/users/login/")
def update_cart_view(request, pk):
    if request.method == "POST":
        product = get_object_or_404(PlantationProduct, pk = pk)
        cart = PlantationCartModel.objects.filter(user = request.user).first()
        quantity = request.POST.get("quantity")

        if not cart:
            return redirect("main:main")
        
        item = cart.items.filter(product = product).first()
        if item and quantity:
            item.define(quantity)
            cart.save()      

    return redirect("cart")

def remove_from_cart_view(request, pk):
    product = get_object_or_404(PlantationProduct, pk = pk)
    cart = PlantationCartModel.objects.filter(user = request.user).first()

    if not cart:
        return redirect("main:main")

    item = cart.items.filter(product = product).delete()
    # cart.items = item
    cart.save()
    

    return redirect("cart")

@login_required(login_url="/users/login/")
def checkout_view(request):
    order_form = PlantationOrderForm()
    address_form = PlantationAddressForm()
    card_form = PlantationCardInformationForm()
    cart = PlantationCartModel.objects.filter(user = request.user).first()

    if not cart:
        return redirect("cart") # nothing in th cart so go back

    context = { 
        "order_form": order_form,
        "address_form": address_form,
        "card_form": card_form,
        "cart": cart
        }
    
    if request.method == "POST":
        order_form = PlantationOrderForm(request.POST)
        address_form = PlantationAddressForm(request.POST)
        card_form = PlantationCardInformationForm(request.POST)

        print("here is data")
        if order_form.is_valid() and address_form.is_valid() and card_form.is_valid():
            #order_form.is_valid() and address_form.is_valid() and card_form.is_valid()
            card = card_form.save()

            print("everything is valid")
            address = address_form.save()
            order = order_form.save(False)

            order.user = request.user
            order.quantity = cart.total_items
            order.address = address
            order.card_information = card
            order.paid = False
            order.save() # redict to invoice 
            order.products.set(cart.items.all())

            cart.delete()

            # for item in cart.items.all():
            #     order.products.add(item) ## then clear cart after successful payment

            # order.add_products(cart.items.all())
            return redirect("item-invoice", order.pk)

    #"user", "paid", "products", "quantity", "address", "card_information"
    
    ## i need products, quantity, address, card
    return render(request, "checkout.html", context)