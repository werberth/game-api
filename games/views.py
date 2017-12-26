from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Game
from .serializers import GameSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().reder(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def game_list(request):
    if request.method == 'GET':
        games = Game.objects.all()
        games_serializer = GameSerializer(
            games, many=True
        )
        return JSONResponse(games_serializer.data)

    elif request.method == 'POST':
        game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JSONResponse(
                game_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return JSONResponse(
            game_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
