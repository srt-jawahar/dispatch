from django.db import models


class Plants(models.Model):
    PLANT = models.CharField(max_length=4, db_column='plant', unique=True)
    PL_DESP = models.CharField(max_length=30, db_column='plant_desc')
    PL_ADRS = models.CharField(max_length=240, db_column='plant_address',null=True, blank=True)
    PSTAT = models.CharField(max_length=1, db_column='process_status')

    class Meta:
        db_table = 'plants'



class Customers(models.Model):
    CUST_ID = models.CharField(max_length=10, db_column='customer_code', unique=True)
    CUST_NAME = models.CharField(max_length=15, db_column='customer_name',null=True, blank=True)
    CUST_ADRS = models.CharField(max_length=240, db_column='customer_address',null=True, blank=True)
    PSTAT = models.CharField(max_length=1, db_column='process_status')

    class Meta:
        db_table = 'customers'


class DeliveryDetails(models.Model):
    DEL_NO = models.CharField(max_length=10, db_column='delivery_no')
    DEL_ITEM = models.BigIntegerField(db_column='delivery_item')
    MATERIAL = models.CharField(max_length=20, db_column='material')
    QUANTITY = models.DecimalField(max_digits=13, decimal_places=2, db_column='quantity')
    QTY_UOM = models.CharField(max_length=3, db_column='qty_uom')
    GROSS_WGT = models.DecimalField(max_digits=13, decimal_places=2, db_column='gross_weight')
    GW_UOM = models.CharField(max_length=3, db_column='gw_uom')
    MAT_DIM = models.CharField(max_length=32, db_column='mat_dim')
    VOLUME = models.DecimalField(max_digits=13, decimal_places=2, db_column='volume')
    VOL_UOM = models.CharField(max_length=3, db_column='vol_uom')
    TOT_WGT = models.DecimalField(max_digits=15, decimal_places=2, db_column='total_weight')
    CUSTOMER = models.CharField(max_length=10, db_column='customer')
    REGION = models.CharField(max_length=10, db_column='region')
    PSTAT = models.CharField(max_length=1, db_column='process_status')

    class Meta:
        db_table = 'delivery_details'