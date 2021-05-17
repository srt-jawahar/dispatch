from django.db import models


# Create your models here.
class TruckDetails(models.Model):
    truck_type = models.CharField(max_length=255)
    length_in_feet = models.FloatField()
    width_in_feet = models.FloatField()
    height_in_feet = models.FloatField()
    length_in_meter = models.FloatField()
    width_in_meter = models.FloatField()
    height_in_meter = models.FloatField()
    truck_total_weight = models.FloatField()
    truck_total_weight_uom = models.CharField(max_length=255)
    truck_max_capacity = models.FloatField()
    truck_min_capacity = models.FloatField()
    truck_capacity_uom = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField()
