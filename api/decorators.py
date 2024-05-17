from api.models import Todos
from rest_framework import serializers

def object_deleted(fn):
    def wrapper(request, *args, **kwargs):
        id=kwargs.get("pk")
        todo_object=Todos.objects.get(id=id)
        if todo_object.is_active==False:
            raise serializers.ValidationError("Task does not exist")
        else:
            return fn(request, *args, **kwargs)
    return wrapper
            

def owner_permission(fn):
    def wrapper(request, *args, **kwargs):
        id=kwargs.get("pk")
        todo_object=Todos.objects.get(id=id)
        if request.user != todo_object.user:
            raise serializers.ValidationError("permission denied")
        else:
            return fn(request, *args, **kwargs)
    return wrapper
