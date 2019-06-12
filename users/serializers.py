from rest_framework.serializers import ModelSerializer
from .models import CustomerUser, Post
from rest_framework.fields import ReadOnlyField

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ['email', 'username']

class PostSerializer(ModelSerializer):
    author_username = ReadOnlyField(source='author.username') #다른사람이 내 아이디 도용 못하게!

    class Meta:
        model = Post
        fields = ['id','author_username','message']