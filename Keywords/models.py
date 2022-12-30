from django.db import models

# Create your models here.
class Keyword(models.Model):
    Kname=models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.Kname)