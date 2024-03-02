from django.db import models

class Advisor(models.Model):
    name=models.CharField(max_length=250)
    adv_id=models.CharField(max_length=200)
    def __str__(self):
        return self.name
