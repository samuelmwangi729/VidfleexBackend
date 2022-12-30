from django.db import models
from Movies.models import Movie
# Create your models here.
class Trailer(models.Model):
    MovieName=models.OneToOneField(Movie,on_delete=models.PROTECT,primary_key=True)
    Link=models.URLField(max_length=300)
    Poster=models.CharField(max_length=300)
    createdAt=models.DateTimeField(auto_now=False,auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return "%s" % (self.MovieName)

    class Meta:
        ordering=['MovieName']