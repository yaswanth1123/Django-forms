from django.db import models

# Create your models here.
class school(models.Model):
    sid=models.PositiveIntegerField(primary_key=True)
    sname=models.CharField(max_length=100)

    def __str__(self):
        return self.name
