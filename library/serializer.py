from rest_framework.serializers import ModelSerializer
from .models import Category,Author,Books,User

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__" 

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email","password","username"] 
