import datetime

from django.db import models
from django.utils import timezone

class Artifact(models.Model):
    text = models.CharField(max_length=200)
    info = models.TextField(blank = True)
    discovered_by = models.CharField(max_length=200, default="unknown")
    pub_date = models.DateTimeField('Date Published', default=datetime.datetime.now)

    def __str__(self):
        return f'{self.text} : {self.info[:25]}...'

class Location(models.Model):
    artifact = models.ForeignKey(Artifact, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text