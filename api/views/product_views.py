from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.response import Response 
from api.models import Product
from api.serializers import ProductSerializer
from rest_framework import status

@api_view(['GET'])
def getProducts(request):
	products = Product.objects.all()
	serializer = ProductSerializer(products, many=True) #True - many items
	return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
	product = Product.objects.get(_id=pk) #primary key by id
	serializer = ProductSerializer(product, many=False) #false - single item
	return Response(serializer.data)

@api_view(['GET'])
def deleteProduct(request, pk):
	product = Product.objects.get(_id=pk) #primary key by id
	serializer = ProductSerializer(product, many=False) #false - single item
	return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user

    product = Product.objects.create(
        user=user,
        name='Sample Name',
        price=0,
        brand='Sample Brand',
        countInStock=0,
        category='Sample Category',
        description=''
    )

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)