from django.db import models


# Create your models here.
class members(models.Model):
    Id = models.AutoField(primary_key=True)
    real_name = models.CharField(max_length=64)
    tz = models.CharField(max_length=128)
    start_datetime = models.DateTimeField()
    start_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

def __str__(self):
        return self.Id,self.real_name,self.tz,self.start_datetime,self.start_date,self.start_time,self.end_datetime,self.end_date,self.end_time