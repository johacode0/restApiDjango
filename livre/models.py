from django.db import models

# Create your models here.
class livre(models.Model):
    titre=models.CharField(max_length=100)
    auteur=models.CharField(max_length=60)
    prix=models.IntegerField(default=0)
    description=models.TextField(null=True)
    def __str__(self):
        return self.titre
