from rest_framework import serializers
from Movies.models import Movie
from Cast.models import Cast
from Genres.models import Genre
from Trailers.models import Trailer
class MovieSerializer(serializers.ModelSerializer):
    Genres = serializers.StringRelatedField(many=True)
    MovieKeywords = serializers.StringRelatedField(many=True)
    class Meta:
        model = Movie
        fields=[
            'Title',
            'Slug',
            'Description',
            'Plot',
            'YoR',
            'CoR',
            'MovieLength',
            'StarRatings',
            'Banner',
            'Genres',
            'MovieKeywords',
            'RandomId',
        ]
class CastSerializer(serializers.ModelSerializer):
    ActorMovie = serializers.StringRelatedField()
    class Meta:
        model = Cast
        fields=[
            'Name',
            'ActorId',
            'ActorMovie',
            'Role'
        ]
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields=[
            'Name',
            'Banner'
        ]
class TrailerSerializer(serializers.ModelSerializer):
    MovieName = serializers.StringRelatedField()
    class Meta:
        model = Trailer
        fields=[
            'MovieName',
            'Link',
            'Poster',
        ]