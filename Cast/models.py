from django.db import models
from Movies.models import Movie
# Create your models here.
class Cast(models.Model):
    Name=models.CharField(max_length=100)
    ActorId=models.CharField(max_length=100)
    ActorMovie = models.ForeignKey(Movie,on_delete=models.PROTECT,related_name="movie")
    Role=models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.Name)