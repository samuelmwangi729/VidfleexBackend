from django.db import models

# Create your models here.
class Contact(models.Model):
    ClientName=models.CharField(max_length=50)
    Email=models.EmailField(max_length=100)
    Message=models.TextField(blank=False)
    createdAt=models.DateField(auto_now=False,auto_now_add=True)


    def __str__(self):
        return "%s" % self.ClientName