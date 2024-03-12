from rest_framework import serializers

from .models import Cart, CartOrder, CartOrderItem, Copoun, Wishlist


class CartSerializer(serializers.ModelSerializer):
    """
    Cart Model Serializer
    """
    class Meta:
        model = Cart 
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(CartSerializer, self).__init__(*args, **kwargs)
        
        request = self.context.get('request')    

        if request and request.method == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 5


class CartOrderSerializer(serializers.ModelSerializer):
    """
    Cart Order Model Serializer
    """
    class Meta:
        model = CartOrder 
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(CartOrderSerializer, self).__init__(*args, **kwargs)
        
        request = self.context.get('request')    

        if request and request.method == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 5


class CartOrderItemSerializer(serializers.ModelSerializer):
    """
    Cart Order Item Model Serializer
    """
    class Meta:
        model = CartOrderItem 
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(CartOrderItemSerializer, self).__init__(*args, **kwargs)
        
        request = self.context.get('request')    

        if request and request.method == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 5


class CopounSerializer(serializers.ModelSerializer):
    """
    Copoun Model Serializer
    """
    class Meta:
        model = Copoun 
        fields = "__all__"


class WishlistSerializer(serializers.ModelSerializer):
    """
    Wish List Model Serializer
    """
    class Meta:
        model = Wishlist 
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(WishlistSerializer, self).__init__(*args, **kwargs)
        
        request = self.context.get('request')    

        if request and request.method == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 5
