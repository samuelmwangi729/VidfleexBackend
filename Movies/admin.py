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
@admin.action(description='Make Marked Latest')
def make_latest(Movie, request, queryset):
    queryset.update(Status='latest')
@admin.action(description='Make Banner')
def make_banner(Movie, request, queryset):
    queryset.update(Status='Banner')
@admin.action(description='Make Marked Upcoming')
def make_upcoming(Movie, request, queryset):
    queryset.update(Status='upcoming')
@admin.action(description='Make Marked Top Rated')
def make_top(Movie, request, queryset):
    queryset.update(Status='top')
@admin.action(description='Make Marked Suggested')
def make_suggested(Movie, request, queryset):
    queryset.update(Status='suggested')
@admin.action(description='Make Marked Trending')
def make_trending(Movie, request, queryset):
    queryset.update(Status='trending')
@admin.action(description='Recommend Marked Movies')
def make_recommended(Movie, request, queryset):
    queryset.update(Status='recommended')
@admin.action(description='Make Marked Popular')
def make_popular(Movie, request, queryset):
    queryset.update(Status='popular')
@admin.action(description='Make Marked Special')
def make_special(Movie, request, queryset):
    queryset.update(Status='special')
@admin.action(description='Set Banners to Images')
def make_image(Movie, request, queryset):
    data=list(queryset.values())
    queryset.update(Image=data[0]['Banner'])
@admin.action(description="Award Movie of the Year")
def make_movieYear(Movie,request,queryset):
    queryset.update(Status="MOY")
@admin.action(description="Most Popular")
def make_mostpopular(Movie,request,queryset):
    queryset.update(Status="MOST")
class MovieAdmin(admin.ModelAdmin):
    change_list_template = "Admin/Movies.html"
    actions=[
        make_image,
        make_mostpopular,
        make_featured,
        make_latest,
        make_upcoming,
        make_top,
        make_suggested,
        make_trending,
        make_recommended,
        make_popular,
        make_special,
        make_banner,
        make_movieYear
    ]
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
        elif obj.Status == 'latest':
            return format_html(f'<div class="badge badge-sm badge-primary" style="background-color:red;color:white">{obj.Status}</div>')
        elif obj.Status == 'upcoming':
            return format_html(f'<div class="badge badge-sm badge-primary" style="background-color:purple;color:white">{obj.Status}</div>')
        elif obj.Status == 'top':
            return format_html(f'<div class="badge badge-sm badge-primary" style="background-color:green;color:white">{obj.Status}</div>')
        elif obj.Status == 'suggested':
            return format_html(f'<div class="badge badge-sm badge-primary" style="background-color:deeppink;color:white">{obj.Status}</div>')
        elif obj.Status == 'trending':
            return format_html(f'<div class="badge badge-sm badge-primary" style="background-color:deepblue;color:white">{obj.Status}</div>')
        elif obj.Status == 'recommended':
            return format_html(f'<div class="badge badge-sm badge-primary" style="background-color:magenta;color:white">{obj.Status}</div>')
        elif obj.Status == 'popular':
            return format_html(f'<div class="badge badge-sm badge-primary" style="background-color:cyan;color:white">{obj.Status}</div>')
        elif obj.Status == 'special':
            return format_html(f'<div class="badge badge-sm badge-primary" style="background-color:indigo;color:white">{obj.Status}</div>')
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
        image=data['image_url']
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
                Image=image,
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