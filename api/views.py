from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PeopleSerializer
@api_view(['GET','POST'])
def index(request):
    data1={
            'name':'bikram',
            'age':12,
            'skills':['python','js','sql'],
        }
    if request.method=="GET":
        print(request.GET.get('search'))
        print('GET method hit')
        return Response(data1)
    elif request.method=="POST":
        print(request.data['age'])
        print('POST method HIT')
        return Response(data1)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def people(request):
    if request.method=="GET":
        objs=Person.objects.all()
        serializer=PeopleSerializer(objs,many=True)
        return Response(serializer.data)
    
    elif request.method=="POST":
        data=request.data
        serializer=PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method=="PUT":
        data=request.data
        obj=Person.objects.get(id=data['id'])

        serializer=PeopleSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method=="PATCH":
        data=request.data
        obj=Person.objects.get(id=data['id'])

        serializer=PeopleSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data=request.data
        obj=Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message':f'person deleted {obj}'})