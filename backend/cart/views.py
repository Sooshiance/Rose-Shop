from django.conf import settings

from rest_framework import generics, permissions, response, status

from .models import Cart
from .serializers import CartSerializer, CartOrderSerializer, CartOrderItemSerializer


User = settings.AUTH_USER_MODEL


class CartAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def create(self, request, *args, **kwargs):
        info = request.data 

        product = info['product'] 
        user = info['user'] 
        quantity = info['quantity'] 
        price = info['price'] 
        shipping = info['shipping'] 
        color = info['color'] 

        cart = Cart.objects.filter(user=user, product=product).first()

        if cart:
            cart.product = product
            cart.quantity = quantity
            cart.price = price
            cart.subtotal = quantity * price
            cart.shipping = shipping * quantity
            cart.color = color
            cart.total = cart.subtotal + cart.shipping

            cart.save()
        else:
            subtotal = quantity * price
            shipping = shipping * quantity
            total = subtotal + shipping
            cart = Cart.objects.create(user=user,product=product,price=price,quantity=quantity,
                                       subtotal=subtotal,shipping=shipping,color=color,total=total)
            cart.save()
        return response.Response(data=request.data, status=status.HTTP_201_CREATED)
