from django.db import models
# Create your models here.
class Genre(models.Model):
    Name=models.CharField(max_length=50,help_text="The Genre Name In Sentense Case")
    Banner=models.ImageField(upload_to="Genres",default="none")

    def __str__(self):
        return "%s" % (self.Name)