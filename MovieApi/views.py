from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import MovieSerializer,CastSerializer,GenreSerializer,TrailerSerializer
from Movies.models import Movie
from Cast.models import Cast
from Genres.models import Genre
from Trailers.models import Trailer
import json
from Contact.models import Contact
from django.http import JsonResponse
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
class LatestList(generics.ListAPIView):
    queryset = Movie.latest.all()
    serializer_class = MovieSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data)
class UpcomingList(generics.ListAPIView):
    queryset = Movie.upcoming.all()
    serializer_class = MovieSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data)
class FeaturedList(generics.ListAPIView):
    queryset = Movie.featured.all()
    serializer_class = MovieSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data)
class TopList(generics.ListAPIView):
    queryset = Movie.top.all()
    serializer_class = MovieSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data)
class SuggestedList(generics.ListAPIView):
    queryset = Movie.suggested.all()
    serializer_class = MovieSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data)
class TrendingList(generics.ListAPIView):
    queryset = Movie.trending.all()
    serializer_class = MovieSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data)
class RecommendedList(generics.ListAPIView):
    queryset = Movie.recommended.all()
    serializer_class = MovieSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data)
class PopularList(generics.ListAPIView):
    queryset = Movie.popular.all()
    serializer_class = MovieSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data)
class SpecialList(generics.ListAPIView):
    queryset = Movie.special.all()
    serializer_class = MovieSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data)
class BannerList(generics.ListAPIView):
    queryset = Movie.objects.filter(Status="Banner")
    serializer_class = MovieSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data)
class SlidersList(generics.ListAPIView):
    queryset = Movie.objects.filter(Status="Sliders")
    serializer_class = MovieSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset,many=True)
        return Response(serializer.data)
class MovieofTheYear(generics.ListAPIView):
    queryset = Movie.objects.filter(Status="MOY").last()
    serializer_class = MovieSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset,many=False)
        return Response(serializer.data)
class MostPopular(generics.ListAPIView):
    queryset = Movie.objects.filter(Status="MOST").first()
    serializer_class = MovieSerializer

    def list(self,request):
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset,many=False)
        return Response(serializer.data)
class getMessage(generics.CreateAPIView):
    def post(self,request):
        data = json.loads(request.body)
        clientName= data['name']
        clientEmail = data['email']
        clientMessage = data['message']
        contact = Contact.objects.create(
            ClientName = clientName,
            Email = clientEmail,
            Message = clientMessage
        )
        message={'data':'Message Successfully Sent'}
        return JsonResponse(message)