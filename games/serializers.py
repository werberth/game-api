from rest_framework import serializers
from games.models import (
    GameCategory,
    Game,
    Player,
    PlayerScore
)


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='game-detail'
    )

    class Meta:
        model = GameCategory
        fields = (
            'url',
            'pk',
            'name',
            'games'
        )


class GameSerializer(serializers.ModelSerializer):
    # We want to display the game category's name instead of the id
    game_category = serializers.SlugRelatedField(
        queryset=GameCategory.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Game
        fields = (
            'url',
            'name',
            'release_date',
            'game_category',
            'played'
        )
