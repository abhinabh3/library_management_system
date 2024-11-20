from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from .models import Category,Author,Books,User
from .serializer import CategorySerializer, AuthorSerializer, BooksSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
# Create your views here.


class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ["name"]

    


class AuthorViewset(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    search_fields = ["name"]



class BooksViewset(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    filterset_fields = ["category","author"]
    search_fields = ["name","author__name","category__name"]
    

@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    user = authenticate(username = email,password=password)
    if user == None:
        return Response("Invalid")
    else:
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key)


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    password = request.data.get("password")
    hash_password = make_password(password)
    request.data["password"] = hash_password
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Data created")
    else:
        return Response(serializer.errors)



