from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Article
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email')

class ArticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"