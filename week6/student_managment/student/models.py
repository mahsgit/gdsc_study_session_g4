from django.db import models
from advisor.models import Advisor



class Student(models.Model):
    name=models.CharField(max_length=250)
    stud_id=models.CharField(max_length=250)
    def __str__(self):
        return self.name
Advisor =models.ForeignKey(Advisor,  on_delete=models.CASCADE)











