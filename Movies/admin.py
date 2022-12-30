from django.contrib import admin
from .models import Movie
from Genres.models import Genre
from Keywords.models import Keyword
from Trailers.models import Trailer
import random,string
from django.utils.html import format_html
from rest_framework.response import Response
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import path 
import json
from rest_framework import status
from Cast.models import Cast
def generate():
    characters=string.ascii_letters + string.digits
    randomId = ''.join(random.choice(characters) for i in range(8))
    return str(randomId)
@admin.action(description='Make Marked Featured')
def make_featured(Movie, request, queryset):
    queryset.update(Status='featured')
class MovieAdmin(admin.ModelAdmin):
    change_list_template = "Admin/Movies.html"
    actions=[make_featured]
    listDisplay=(
        'img_preview',
        'RandomId',
        'Title',
        'YoR',
        'CoR',
        'MovieLength',
        'get_rating',
        'get_status',
        'get_cast',
    )
    def get_rating(self,obj):
        return format_html(f'{obj.StarRatings} Stars')
    def get_status(self,obj):
        if obj.Status == 'featured':
            return format_html(f'<div class="badge badge-sm badge-primary">{obj.Status}</div>')
        else:
             return format_html(f'<div class="badge badge-sm badge-warning text-white">{obj.Status}</div>')
    def img_preview(self,obj): #new
        return format_html('<img src = "{url}" style="width:30px !important"/>'.format(
             url = obj.Banner
         ))
    def get_cast(self,obj):
        return format_html(f'<button class="btn btn-success btn-sm" type="button" onclick=getCast("{obj.MovieId}")>get Cast</button>')
    list_display=listDisplay
    prepopulated_fields = {"Slug": ("Title",)}
    list_filter = (
        'StarRatings',
        'CoR',
        'YoR',
    )
    def get_urls(self):
        urls=super().get_urls()
        custom_urls=[
            path("postVideos/",self.saveVideos),
            path("postCast/",self.saveCast),
        ]
        return custom_urls + urls
    def saveCast(self,request):
        data = json.loads(request.body)
        cRole=data['role']
        actor=data['actorId']
        actorName=data['name']
        actorMovie=data['movie']
        #get the movie 
        movieInstance = Movie.objects.filter(MovieId=actorMovie).first()
        #check if the actor exists in the same movie 
        if Cast.objects.filter(Name=actorName,ActorMovie=movieInstance).exists():
            pass
        else:
            Cast.objects.create(Name=actorName,ActorId=actor,ActorMovie=movieInstance,Role=cRole)
        return JsonResponse(data={'message':'Cast Successfully Added','status':'success'},status=status.HTTP_200_OK)
    def saveVideos(self,request):
        data = json.loads(request.body)
        movieId=data['imdb_id']
        title=data['title']
        slug=str(title).replace(" ","-")
        description=data['description']
        yor = data['year']
        cor=data['content_rating']
        movielength=data['movie_length']
        starating=data['rating']
        plot=data['plot']
        banner=data['banner']
        genres=data['gen'] #array 
        keywords = data['keywords'] #array
        trailer = data['trailer']
        randomId=generate()
        genresArray=[]
        keywordsArray=[]
        #create Genres and get the instance 
        for genre in genres:
            #create
            #check if the genre exists 
            if Genre.objects.filter(Name=genre['genre']).exists():
                pass
            else:
                gInstance=Genre.objects.create(Name=genre['genre'])
                if gInstance:
                    genresArray.append(gInstance)
        #create keywords 
        for keyword in keywords:
            #create the keyword in the database
            if Keyword.objects.filter(Kname=keyword['keyword']).exists():
                pass
            else:
                kInstance=Keyword.objects.create(Kname=keyword['keyword'])
                if kInstance:
                    keywordsArray.append(kInstance)
        #create the movie now 
        if Movie.objects.filter(MovieId = movieId).exists():
            pass
        else:
            movieInstance=Movie.objects.create(
                MovieId=movieId,
                Title = title,
                Slug=slug,
                Description=description,
                Plot=plot,
                YoR=yor,
                CoR=cor,
                MovieLength=movielength,
                StarRatings=starating,
                Banner=banner,
                RandomId=randomId,
            )
            movieInstance.Genres.set(genresArray)
            movieInstance.MovieKeywords.set(keywordsArray)
            if movieInstance:
                #create a trailer 
                if Trailer.objects.filter(MovieName=movieInstance).exists():
                    pass
                else:
                    #create the trailer 
                    Trailer.objects.create(
                        MovieName=movieInstance,
                        Link=trailer,
                        Poster=banner
                    )
            return JsonResponse(data={'message':'Cast Successfully Added','status':'success'},status=status.HTTP_200_OK)
admin.site.register(Movie,MovieAdmin)