from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer,ArticeSerializer
from rest_framework import viewsets
from .models import Article
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view



class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#FBV @api_view
@api_view(['GET'])
def article_list(request):
    '''
    获取所有文章
    '''
    if request.method=='GET':
        response_data = ArticeSerializer(instance=Article.objects.all(),many=True)
        return Response(response_data.data,status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def article_detail(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(data={'msg':'没有此课程的信息'},status=status.HTTP_404_NOT_FOUND)
    else:
        if request.method == "GET":
            article_data = ArticeSerializer(instance=article)
            return Response(article_data.data,status=status.HTTP_200_OK)





