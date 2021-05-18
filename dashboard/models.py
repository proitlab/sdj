from django.db import models

# Create your models here.

class Dashboard(models.Model):
#    proxy = True

    class Meta:
        verbose_name_plural = 'Dashboard'
        app_label = 'dashboard'