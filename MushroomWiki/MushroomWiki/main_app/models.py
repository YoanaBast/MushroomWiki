from django.core.validators import MinLengthValidator
from django.db import models

from .validators import only_letters_spaces


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Mushroom(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(2), only_letters_spaces])
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='mushrooms')