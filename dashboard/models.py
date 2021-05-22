from django.db import models

# Create your models here.

class Chart(models.Model):
#    proxy = True

    class Meta:
        verbose_name_plural = 'Charts'
