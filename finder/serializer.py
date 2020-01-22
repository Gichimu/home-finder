from rest_framework import serializers
from .models import Property

class proSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['name', 'description', 'price', 'size_length', 'size_width', 'size_total']