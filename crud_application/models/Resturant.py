from django.db import models

class Resturant(models.Model):

    resturantName = models.CharField(max_length=50)
    startCount = models.IntegerField(blank=True)
    managerFullName = models.CharField(max_length=50)

    def __str__(self):
        return self.resturantName

class Branches(models.Model):

    streetName = models.CharField(max_length=50)
    cityName = models.CharField(max_length=50)
    countryName = models.CharField(max_length=50)
    fullAddress = models.CharField(max_length=50)
    resturantId = models.ForeignKey(Resturant, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullAddress        