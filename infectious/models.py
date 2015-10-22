from django.db import models

# Create your models here.


class RiskManagement(models.Model):
    risk_inspection = models.TextField(verbose_name='')
    risk_information = models.TextField(verbose_name='')
    risk_information_photo = models.ImageField()