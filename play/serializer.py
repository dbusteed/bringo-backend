from rest_framework import serializers
from play.models import Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'name', 'tiles', 'owner')

    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data