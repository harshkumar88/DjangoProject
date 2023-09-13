from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60,unique=True,null=False)
    class Meta:
        db_table = 'MyHeroes'

    def __str__(self):
        return self.name 
