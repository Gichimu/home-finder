from django.shortcuts import render, redirect, Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Property
from .serializer import proSerializer   
from .forms import propertyForm 
from .permissions import IsAdminOrReadOnly

def home(request):
    form = propertyForm()
    try:
        properties = Property.objects.all()
    except Property.DoesNotExist:
        properties = None
    return render(request, 'index.html', {'form':form, 'properties':properties})

def save(request):
    form = propertyForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('home')


class proList(APIView):
    def get(self, request, format=None):
        all_properties = Property.objects.all()
        serializers = proSerializer(all_properties, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = proSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAdminOrReadOnly,)


class proDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_property(self, pk):
        try:
            return Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        property = self.get_property(pk)
        serializers = proSerializer(property)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        property = self.get_property(pk)
        serializers = proSerializer(property, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        property = self.get_property(pk)
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

