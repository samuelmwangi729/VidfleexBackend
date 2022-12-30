from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import MovieSerializer,CastSerializer,GenreSerializer,TrailerSerializer
from Movies.models import Movie
from Cast.models import Cast
from Genres.models import Genre
from Trailers.models import Trailer
import json
# Create your views here.

class MoviesList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    def List(self,request):
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data)
class MoviesPosts(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def POST(self,request):
        data = json.loads(request.body)
        return Response(data)
class CastsList(generics.ListAPIView):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer

    def List(self,request):
        queryset=self.get_queryset()
        serializer = CastSerializer(queryset,many=True)

        return Response(serializer.data)
class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def List(self,request):
        queryset = self.get_queryset()
        serializer = GenreSerializer(queryset,many=True,context= 
        {'request': request})
        return Response(serializer.data)
class TrailerList(generics.ListAPIView):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = TrailerSerializer(queryset,many=True)
        return Response(serializer.data)