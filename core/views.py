from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken,PostSerializer
from .models import demo
from django.core import serializers
from rest_framework.parsers import JSONParser

from rest_framework import viewsets
import json
from rest_framework.generics import CreateAPIView


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    
    try:
        Demo = demo.objects.all()
    except demo.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'POST':
        print(request.user.username)
        
        print(request.data)
        # data = JSONParser().parse(request)
        serializer = PostSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            print("????????????????????")
            serializer.save(user=request.user)
            return JsonResponse(serializer.data, status=201)
        print(serializer.errors)    
        return JsonResponse(serializer.errors, status=400)    
    elif request.method == 'GET':
        snippets = demo.objects.all()
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        serializer = PostSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)    