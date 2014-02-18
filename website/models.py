from django.db import models
from datetime import datetime, timedelta

class FoodTruck(models.Model):
  name = models.CharField(max_length=30)
  location = models.CharField(max_length=300)
  start_date = models.DateField()
  start_time = models.TimeField(null=True, blank=True)

  def __unicode__(self):
    return self.name 

  def save(self, **kwargs):
    ft = FoodTruck.objects.filter(name = self.name, 
                                  location = self.location)
    if not ft:
      super(FoodTruck, self).save(**kwargs)

  def last_month():
    now = datetime.now()
    start = datetime.min.replace(year=now.year, month=now.month,
                                 day=now.day)
    end = (start + timedelta(days=30)) - timedelta.resolution
    return (start, end)
