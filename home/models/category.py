from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=5000)
    gender = models.CharField(max_length=5000, default='')

    def __str__(self):
        return self.name
