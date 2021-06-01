from django.db import models
from masterdata.models import DateAuditModel, UserAuditModel


class FreightOrders(DateAuditModel, UserAuditModel):
    status = (
        ("Suggested", "Initial suggest status"),
        ("Open", "Open status to take decision"),
        ("Confirmed", "Confirmation status"),
    )
    freight_order_no = models.CharField(max_length=30, unique=True)
    delivery_id = models.ManyToManyField('masterdata.DeliveryHeaders')
    delivery_no = models.CharField(max_length=10)
    total_volume = models.DecimalField(max_digits=13, decimal_places=2)
    total_weight = models.DecimalField(max_digits=15, decimal_places=2)
    from_location = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    suggested_truck_type = models.CharField(max_length=30)
    no_of_trucks = models.IntegerField()
    truck_status = models.CharField(choices=status, max_length=30, default='Suggested')
    transportor_name = models.CharField(max_length=255, null=False, blank=True)

    class Meta:
        db_table = 'freight_orders'
