from rest_framework import serializers

from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            'name',
            'id',
            'release_date',
            'game_category',
            'played'
        )
