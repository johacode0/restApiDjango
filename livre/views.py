from pickle import GET
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LivreSerializer
from .models import livre


# Create your views here.
@api_view(['GET'])
def allBooks(request):
    books =livre.objects.all()
    serializers=LivreSerializer(books,many=True)
    return Response(serializers.data)



@api_view(['GET'])
def getBook(request, id):
    book =livre.objects.get(id=id)
    serializers=LivreSerializer(book)
    return Response(serializers.data)


@api_view(['POST'])
def addBooks(request):
    serializers=LivreSerializer(data=request.data, many=True)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)





    
@api_view(['PUT'])
def updateBook(request, id):
    book=livre.objects.get(id=id)
    serializers=LivreSerializer(instance=book ,data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)
@api_view(['DELETE'])
def delbook(request, id):
    book =livre.objects.get(id=id)
    book.delete()
    return Response("confirmation n !")