import django_filters
from rest_framework import filters

from .models import PlayerScore


class PlayerScoreFilter(filters.FilterSet):
    min_score = django_filters.NumberFilter(
        name='score',
        lookup_expr='gte'
    )
    max_score = django_filters.NumberFilter(
        name='score',
        lookup_expr='gte'
    )
    from_score_date = django_filters.DateTimeFilter(
        name='score_date',
        lookup_expr='gte'
    )
    to_score_date = django_filters.DateTimeFilter(
        name='score_date',
        lookup_expr='lte'
    )
    player_name = django_filters.AllValuesFilter(
        name='player__name'
    )
    game_name = django_filters.AllValuesFilter(
        name='game__name'
    )

    class Meta:
        model = PlayerScore
        fields = (
            'score',
            'from_score_date',
            'to_score_date',
            'min_score',
            'max_score',
            # player__name will be accessed as player_name
            'player_name',
            # game__name will be accessed as game_name
            'game_name',
        )
