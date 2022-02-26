from rest_framework import serializers
from .models import livre
class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = livre
        fields = '__all__'
