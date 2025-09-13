from django.db import models

class UserStatistic(models.Model):
    user = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    field = models.IntegerField(null=True, blank=True)
    soil_type = models.CharField(max_length=255, null=True, blank=True)
    avarage_price = models.IntegerField(null=True, blank=True)
    climate_class = models.CharField(null=True, blank=True)
    
    def __str__(self):
        return str(self.soil_type)
    
    class Meta:
        verbose_name_plural = "User Data"


class OpenData(models.Model):
    text = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return str(self.text)
    
    class Meta:
        verbose_name_plural = "Open Data Form"