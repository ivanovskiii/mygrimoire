from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="cover_image", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    featured = models.BooleanField(default=0)  # 0 for regular, 1 for featured


class TarotCard(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="tarot_card_image", null=True, blank=True)
    suit = models.CharField(max_length=10, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    isMajorArcana = models.BooleanField(default=0)  # 0 for minor, 1 for major
    cardOfTheDay = models.BooleanField(default=0)   # 1 for "Card Of The Day"
