from rest_framework.generics import ListAPIView
from play.serializer import BoardSerializer
from play.models import Board
from django_filters.rest_framework import DjangoFilterBackend

class BoardList(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)