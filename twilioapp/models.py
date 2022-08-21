from django.db import models


class OTPVerification(models.Model):
    username=models.CharField(max_length=150, default=0)
    otp = models.IntegerField(default=-1)

    def __str__(self):
        return self.name           
