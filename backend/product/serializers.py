from rest_framework import serializers

from .models import Category, Feature, Product, Gallery, Color


class CategorySerializer(serializers.ModelSerializer):
    """
    Category serializer 
    """
    class Meta:
        model = Category
        fields = "__all__"


class FeatureSerializer(serializers.ModelSerializer):
    """
    Fature serializer
    """
    class Meta:
        model = Feature
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    """
    Feature serializer
    """
    class Meta:
        model = Gallery
        fields = '__all__'


class ColorSerialzer(serializers.ModelSerializer):
    """
    Color serializer
    """
    class Meta:
        model = Color
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Product serailizer
    """

    galler = GallerySerializer(many=True, read_only=True)
    color  = ColorSerialzer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'title',
            'category',
            'feature',
            'description',
            'slug',
            'pic',
            'is_stock',
            'price',
            'shipping',
            'is_active',
            'vendor',
            'gallery',
            'color',
        )
    
    def __init__(self, *args, **kwargs):
        super(ProductSerializer, self).__init__(*args, **kwargs)
        
        request = self.context.get('request')    

        if request and request.method == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 5
