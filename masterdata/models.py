from django.db import models


class Plants(models.Model):
    PLANT = models.CharField(max_length=4, db_column='plant', unique=True)
    PL_DESP = models.CharField(max_length=30, db_column='plant_desc')
    PL_ADRS = models.CharField(max_length=240, db_column='plant_address',null=True, blank=True)
    PSTAT = models.CharField(max_length=1, db_column='process_status')

    class Meta:
        db_table = 'plants'
