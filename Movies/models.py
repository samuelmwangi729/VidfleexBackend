from django.db import models
from Genres.models import Genre
from Keywords.models import Keyword
class Movie(models.Model):
    class Latest(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(Status="latest")
    class Upcoming(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(Status="upcoming")
    class Featured(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(Status="featured")
    class Top(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(Status="top")
    class Suggested(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(Status="suggested")
    class Trending(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(Status="trending")
    class Recommended(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(Status="recommended")
    class Popular(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(Status="popular")
    class Special(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(Status="special")
    
    options=(
        ('latest','Latest'),
        ('upcoming','Upcoming'),
        ('featured','Featured'),
        ('top','Top'),
        ('suggested','Suggested'),
        ('trending','Trending'),
        ('recommended','Recommended'),
        ('popular','Popular'),
        ('special','Special'),
    )
    MovieId=models.CharField(max_length=20,help_text="Movie Id from IMDB")
    Title=models.CharField(max_length=200)
    Slug=models.SlugField()
    Description=models.TextField(default="Null")
    Plot=models.TextField(default="Null")
    YoR=models.CharField(max_length=4,help_text="Year of Release")
    CoR=models.CharField(max_length=20,help_text="Content Rating")
    MovieLength=models.CharField(max_length=4,help_text="The Length of the movie in Minutes")
    StarRatings=models.IntegerField(default=0)
    Genres=models.ManyToManyField(Genre,related_name="genres")
    MovieKeywords=models.ManyToManyField(Keyword) #one to many field 
    Banner=models.CharField(max_length=200,help_text="Movie Banner to display")
    Image=models.CharField(max_length=200,help_text="Image to Display to Frontends",default=Banner)
    RandomId=models.CharField(max_length=20)
    objects=models.Manager()
    latest=Latest()
    upcoming=Upcoming()
    featured=Featured()
    top=Top()
    suggested=Suggested()
    trending=Trending()
    recommended=Recommended()
    popular=Popular()
    special=Special()
    Status=models.CharField(max_length=50,choices=options,default='recommended')
    createdAt=models.DateTimeField(auto_now=False,auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return self.Title
    class Meta:
        verbose_name="Movie"
        verbose_name_plural="Movies"
        ordering=['-YoR']