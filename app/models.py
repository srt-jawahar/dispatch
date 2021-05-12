from django.db import models


# Comment added for testing
# Create your models here.
class FreightOrder(models.Model):
    DEL_NO = models.CharField(max_length=255, )
    DEL_ITEM = models.CharField(max_length=255, )
    MATERIAL = models.CharField(max_length=255, )
    QUANTITY = models.FloatField()
    QTY_UOM = models.CharField(max_length=255, )
    GROSS_WGT = models.FloatField()
    GW_UOM = models.CharField(max_length=255, )
    MAT_DIM = models.CharField(max_length=255, )
    VOLUME = models.CharField(max_length=255, )
    VOL_UOM = models.CharField(max_length=255, )
    TOT_WGT = models.FloatField()
    CUSTOMER = models.CharField(max_length=255, )
    REGION = models.CharField(max_length=255, )

    def __str__(self):
        return self.MATERIAL
