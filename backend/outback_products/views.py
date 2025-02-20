from django.shortcuts import get_object_or_404, render
from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly


"""이전 테스트 코드
class FoodView(APIView):

    def get(self, request):
        products = Product.objects.all() 
        serializer = ProductSerializer(products,)
        return Response(serializer.data)
        

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



class FoodDetailView(APIView):

    def get_object(self, pk):  
        return get_object_or_404(Product, pk=pk)  
    
    def get(self, request, pk):  
        products = self.get_object(pk)
        serializer = ProductSerializer(products)
        return Response(serializer.data)
    
    def put(self, request, pk):  
        products = self.get_object(pk)
        serializer = ProductSerializer(products, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, pk): 
        products = self.get_object(pk)
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""    


class ProductViewSet(viewsets.ModelViewSet):
    """    ModelViewSet은 다음 기능을 자동으로 제공

    - list(): GET /products/ (전체 목록 조회)
    - create(): POST /products/ (새 제품 생성)
    - retrieve(): GET /products/<pk>/ (특정 제품 조회)
    - update(): PUT /products/<pk>/ (특정 제품 수정)
    - destroy(): DELETE /products/<pk>/ (특정 제품 삭제)

    """
    queryset = Product.objects.all() # 모든 제품 조회
    serializer_class = ProductListSerializer # 전체 목록 조회
    permission_classes = [IsAdminOrReadOnly] # permissions.py에서 직접 만든 커스텀 권한 적용



    def get_object(self):  # product_id로 조회
        product_id = self.kwargs['pk'] # kwargs : 키워드 인자를 받아옴
        return get_object_or_404(Product, product_id=product_id) # 없으면 404 오류 반환

    def get_serializer_class(self): # 시리얼라이저 클래스 선택
        if self.action == 'list': # list : modelviewset에서 제공하는 기본 기능 [52번 line 참고]
            return ProductListSerializer # 전체 목록 조회
        else:
            return ProductDetailSerializer # 특정 제품 조회
        

