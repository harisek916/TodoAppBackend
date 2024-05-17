from django.shortcuts import render
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import authentication,permissions
from rest_framework import serializers

from api.serializers import UserSerializer,TodoSerializer,TodoUpdateSerializer
from api.models import Todos
from api.decorators import object_deleted,owner_permission

# Create your views here.

class SignUpView(APIView):

    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
class TodoView(viewsets.ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=TodoSerializer
    queryset=Todos.objects.filter(is_active=True)

    def create(self,request,*args,**kwargs):
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def list(self, request, *args, **kwargs):
        qs=Todos.objects.filter(user=request.user,is_active=True)
        serializer=TodoSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    @method_decorator([object_deleted,owner_permission])
    def retrieve(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=Todos.objects.get(id=id)

        
        
        serilaizer=TodoSerializer(qs)
        return Response(data=serilaizer.data)
    
    @method_decorator([owner_permission,owner_permission])
    def update(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        todo_object=Todos.objects.get(id=id)

        
        serializer=TodoUpdateSerializer(data=request.data,instance=todo_object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    @method_decorator([object_deleted,owner_permission])
    def destroy(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        
        Todos.objects.filter(id=id).update(is_active=False)
        return Response(data={"message":"deleted"})
