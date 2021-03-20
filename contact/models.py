from django.db import models

# Create your models here.


class contactus(models.Model):
    fullname = models.CharField(max_length=20, blank=True)
    emailaddress = models.TextField(max_length=200, blank=False)
    primary_no = models.CharField(max_length=12, blank=False)
    comments = models.CharField(max_length=2000,blank=False)


    def __str__(self):
        return self.emailaddress