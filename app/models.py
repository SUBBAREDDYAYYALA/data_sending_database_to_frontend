from django.db import models

# Create your models here.
class sports(models.Model):
    sport_name = models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.sport_name
    
class player(models.Model):

    sports_name = models.ForeignKey(sports,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name