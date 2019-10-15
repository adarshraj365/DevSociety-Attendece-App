from django.db import models

# Create your models here.



class present(models.Model):
    name = models.CharField(max_length = 500)
    branch = models.CharField(max_length = 100)
    mail = models.CharField(max_length=100)
    roll = models.IntegerField(default=0);

    def __str__(self):
        return self.name
