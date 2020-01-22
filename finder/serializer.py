from rest_framework import serializers
from .models import Property

class proSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name', 'description', 'price', 'size_length', 'size_width', 'size_total']