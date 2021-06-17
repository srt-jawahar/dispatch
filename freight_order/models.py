from django.db import models
from masterdata.models import DateAuditModel, UserAuditModel


class FreightOrders(DateAuditModel, UserAuditModel):
    # Constants
    SUGGESTED = 'Suggested'
    OPEN = 'Open'
    CONFIRMED = 'Confirmed'
    ASSIGNED = 'Assigned'

    status = (
        (SUGGESTED, "Initial suggest status"),
        (OPEN, "Open status to take decision"),
        (CONFIRMED, "Confirmation status"),
        (ASSIGNED, "Truck Assign status"),
    )
    freight_order_no = models.CharField(max_length=30, unique=True)
    delivery_no = models.CharField(max_length=10)
    total_volume = models.DecimalField(max_digits=13, decimal_places=2)
    total_weight = models.DecimalField(max_digits=15, decimal_places=2)
    from_location = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    freight_status = models.CharField(choices=status, max_length=30, default=SUGGESTED)
    remarks = models.CharField(max_length=255, null=False, blank=True)

    class Meta:
        db_table = 'freight_orders'

    @property
    def truck_types(self):
        return self.freighttruckassignments_set.all()


class FreightTruckAssignments(DateAuditModel, UserAuditModel):
    freight_order = models.ForeignKey('FreightOrders', on_delete=models.CASCADE)
    freight_order_no = models.CharField(max_length=30)
    suggested_truck_type = models.CharField(max_length=30)
    no_of_trucks = models.IntegerField()
    transportor_name = models.CharField(max_length=255, null=False, blank=True)

    class Meta:
        db_table = 'freight_truck_assignments'
