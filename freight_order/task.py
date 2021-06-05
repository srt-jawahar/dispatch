import django
django.setup()
from truckmanagement.models import TruckAvailability


def reset_no_of_trucks():
    print('Background printing....')
    truck_availabilities = TruckAvailability.objects.all()
    for truck in truck_availabilities:
        truck.no_of_trucks = 0
        truck.no_of_trucks_reserved = 0
        truck.save()
