from django.db import models

# Create your models here.
class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pokedex/', null=True, blank=True)

    def __str__(self):
        return self.name