from rest_framework import serializers
from .models import Product




class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'product_price']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'product_info', 'product_price', 'product_stock']
        extra_kwargs = { # 추가 설정
            'product_stock': {'write_only': True}, # POST에서는 받되, 응답에서는 숨김
            'product_id': {'write_only': True}  # POST에서는 받되, 응답에서는 숨김
        }
    


