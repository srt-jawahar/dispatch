from django.db import models
from masterdata.models import DateAuditModel, UserAuditModel


class FreightOrders(DateAuditModel, UserAuditModel):
    # Constants
    SUGGESTED = 'Suggested'
    OPEN = 'Open'
    CONFIRMED = 'Confirmed'
    ASSIGNED = 'Assigned'

    #TRUCK STATUS
    TOWARDS_SOURCE = 'towards_source'
    REACHED_SOURCE = 'reached_source'
    LOADED = 'loaded'
    TOWARDS_DESTINATION = 'towards_destination'
    REACHED_DESTINATION = 'reached_destination'
    UNLOADING = 'unloading'
    TRIP_CLOSING = 'trip_closing'

    truck_status = (
        (TOWARDS_SOURCE, 'Trip starts towards source destination'),
        (LOADED, 'Truck Loading'),
        (REACHED_SOURCE, 'Truck reached the source'),
        (TOWARDS_DESTINATION, 'Truck starts trip to destination'),
        (REACHED_DESTINATION, 'Truck reached destination'),
        (UNLOADING, 'Truck unloading'),
        (TRIP_CLOSING, 'Truck loaded with the materials'),
    )

    status = (
        (SUGGESTED, "Initial suggest status"),
        (OPEN, "Open status to take decision"),
        (CONFIRMED, "Confirmation status"),
        (ASSIGNED, "Truck Assign status"),
    )

    freight_order_no = models.CharField(max_length=30, unique=True)
    delivery_id = models.ManyToManyField('masterdata.DeliveryHeaders')
    delivery_no = models.CharField(max_length=10)
    total_volume = models.DecimalField(max_digits=13, decimal_places=2)
    total_weight = models.DecimalField(max_digits=15, decimal_places=2)
    from_location = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    freight_status = models.CharField(choices=status, max_length=30, default=SUGGESTED)
    remarks = models.CharField(max_length=255, null=False, blank=True)
    truck_number = models.CharField(max_length=255, null=False, blank=True, default='')
    truck_driver_details = models.CharField(max_length=255, null=False, blank=True, default='')
    truck_current_pos = models.CharField(max_length=255, null=False, blank=True, default='')
    truck_status = models.CharField(choices=truck_status, max_length=30, default='')

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
