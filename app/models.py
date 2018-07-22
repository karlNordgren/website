"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField("artist", max_length=50)
    year_formed = models.PositiveIntegerField()

class Album(models.Model):
    name = models.CharField("album", max_length=50)
    artist = models.ForeignKey(Artist)

class Location(models.Model):
    name = models.CharField("Location", max_length=50)
    Album = models.ForeignKey(Album)


class Card(models.Model):
    name = models.CharField("Card", max_length=50)
    numberInDeck = models.PositiveIntegerField()

class Suit(models.Model):
    suit = models.CharField("Suit", max_length=50)
    card = models.ForeignKey(Card)

class Value(models.Model):
    value = models.CharField("Card Value", max_length=50)
    suit = models.ForeignKey(Suit)
   

