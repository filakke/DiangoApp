from django.shortcuts import get_object_or_404, render, redirect, reverse
from store.models import Cart, Order, ProductApp
 
# Create your views here.

def index(request):
    products = ProductApp.objects.all()
    return render(request, 'store/index.html', context={"products": products})

def product_detail(request,slug):
    product = get_object_or_404(ProductApp, slug=slug)
    return render(request, 'store/detail.html', context={"product":product})

def add_to_cart(request, slug):
    user = request.user # ici on recupere seulemen l'utilisateur, c'est just une association des variable
    # pour eviter de taper request.user chaque fois  
    product = get_object_or_404(ProductApp, slug=slug) # ici on recupere le produit si il l'exist sinon on une erreur avec get_object_or 404  
    # et on lui passe slug, on lui recupere dans le variabe product
    cart, _ = Cart.objects.get_or_create(user=user) # si le produit exist on va recupere le panier de l'utilisateur avec get_or_created, si il exist pas il est crée, au cas contrere on lui recupere dans le variable cart
    order, created = Order.objects.get_or_create(user=user,
                                                 product=product) #  pareille avec order, on cherche dans la bd si l'objet order est associe avec user qui fait la requet qui corespond au produit qu'on souhait ajouter  
    
    if created: # si le produit est cree
        cart.orders.add(order) # on l'ajoute dans le panier
        cart.save() # et on lui sauvgarde
    else:
        order.quantity += 1 # cas contrere c'est a dire il est deja cree au prealable : on encrumente
        order.save()
        
    return redirect(reverse("product", kwargs={"slug": slug}))
        
def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    
    
    return render(request, 'stroe/cart.html', context={"orders": cart.orders.all()})
