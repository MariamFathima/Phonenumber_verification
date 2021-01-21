from django.db import models

class Phone(models.Model):
    Mobile_number = models.CharField(max_length=10,blank=False)
    key = models.CharField(max_length=100,blank=True)
    isVerified = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return str(self.Mobile_number)
