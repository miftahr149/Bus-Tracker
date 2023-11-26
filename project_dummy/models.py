from django.db import models

# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class ListSong(models.Model): 
    for_singer = models.CharField(max_length=30, default='')
    list_song = models.ManyToManyField(Song)

    def __str__(self) -> str:
        return f'{self.for_singer} (id = {self.id})'

class Singer(models.Model):
    name = models.CharField(max_length=30)
    list_song = models.ForeignKey(ListSong, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
