from django.db import models
from masterdata.models import DateAuditModel, UserAuditModel
from django.utils import timezone

import os


def upload_location(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"files/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


class FreightOrders(DateAuditModel, UserAuditModel):
    # Constants
    SUGGESTED = 'Suggested'
    OPEN = 'Open'
    CONFIRMED = 'Confirmed'
    ASSIGNED = 'Assigned'
    CLOSED = 'Closed'

    # TRUCK STATUS
    TOWARDS_SOURCE = 'towards_source'
    REACHED_SOURCE = 'reached_source'
    LOADED = 'loaded'
    TOWARDS_DESTINATION = 'towards_destination'
    REACHED_DESTINATION = 'reached_destination'
    UNLOADING = 'unloading'
    TRIP_CLOSING = 'trip_closing'

    # APPROVAL STATUS
    ACCEPTED = 'Accepted'
    REQUEST = 'Request'
    WAITING = 'Waiting'
    REJECTED = 'Rejected'

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
        (CLOSED, "Truck Task Completed status"),
    )

    approval_status = (
        (ACCEPTED, 'Accepted'),
        (REQUEST, 'Request for additional info'),
        (WAITING, 'Waiting for confirmation'),
        (REJECTED, 'Rejected')
    )

    freight_order_no = models.CharField(max_length=30, unique=True)
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
    total_distance = models.FloatField(default=0, null=False, blank=True)
    dist_uom = models.CharField(max_length=255, default='', null=False, blank=True)
    submission_date = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
    total_amount = models.CharField(max_length=255, default='', null=False, blank=True)
    advance_amount = models.FloatField(default=0, null=False, blank=True)
    approval_status = models.CharField(max_length=255, choices=approval_status, default='', null=False, blank=True)
    document_details = models.FileField(upload_to=upload_location, null=True, blank=True)

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
