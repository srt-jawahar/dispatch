from django.db import models


# Create your models here.
class TruckDetails(models.Model):
    truck_type = models.CharField(max_length=255, unique=True)
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

    def __str__(self):
        return self.truck_type


class TruckAvailability(models.Model):
    class Meta:
        ordering = ['created_at']
    user_detail = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    transportor_name = models.CharField(max_length=255, null=False, blank=True)
    truck_type = models.ForeignKey('TruckDetails', on_delete=models.CASCADE)
    source_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    no_of_trucks = models.CharField(max_length=255)
    availability = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    remarks = models.CharField(max_length=255)
    no_of_trucks_reserved = models.IntegerField()

    def __str__(self):
        return self.transportor_name
