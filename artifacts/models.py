import datetime

from django.db import models
from django.utils import timezone

class Location(models.Model):
    image = models.ImageField(upload_to = 'artifacts/uploads', default = 'artifacts/uploads/qmark.png')    
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Artifact(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default = 1)
    text = models.CharField(max_length=200)
    info = models.TextField(blank = True)
    discovered_by = models.CharField(max_length=200, default="unknown")
    pub_date = models.DateField('Date Published', default=datetime.date.today)
    image = models.ImageField(upload_to = 'artifacts/uploads', default = 'artifacts/uploads/qmark.png')

    def __str__(self):
        return f'{self.text} : {self.info[:25]}...'
