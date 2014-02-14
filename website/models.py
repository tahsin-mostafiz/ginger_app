from django.db import models
from datetime import datetime, timedelta

class FoodTruck(models.Model):
  name = models.CharField(max_length=30)
  location = models.TextField()
  creation_date = models.DateTimeField(default=datetime.now)
  start_date = models.DateTimeField(null=True, blank=True)

  def __unicode__(self):
    return self.name 


