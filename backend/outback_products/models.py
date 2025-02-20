from django.db import models


class Product(models.Model):
    product_id = models.CharField(max_length=50, primary_key= True) # 음식 id
    product_name = models.CharField(max_length=50)                  # 음식 이름
    product_info = models.TextField()                               # 음식 설명
    product_price = models.PositiveIntegerField() # 0 또는 정수만   # 가격
    product_stock = models.PositiveIntegerField()                   # 재고