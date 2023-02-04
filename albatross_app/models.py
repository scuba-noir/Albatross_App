from django.db import models
import django.utils.timezone

# Create your models here.

class contactFormRecords(models.Model):

    id = models.BigAutoField(primary_key = True)
    date = models.DateField(default = django.utils.timezone.now)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    message = models.CharField(max_length = 250, default = "")