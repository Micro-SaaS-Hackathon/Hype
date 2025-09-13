from django.db import models

class UserStatistic(models.Model):
    field = models.IntegerField(null=True, blank=True)
    soil_type = models.CharField(max_length=255, null=True, blank=True)
    avarage_price = models.IntegerField(null=True, blank=True)
    climate_class = models.CharField(null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.field
    
    class Meta:
        verbose_name_plural = "User Data"