from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models


class Factories(models.Model):
    factoryName = models.CharField(max_length=50)
    factorySince = models.PositiveIntegerField(validators=[MaxLengthValidator(4)])
    factoryAddress = models.CharField(max_length=200, blank=True, null=True)
    factoryManagerFullName = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.factoryName + ' ' + str(
            self.factorySince) + ' ' + self.factoryAddress + ' ' + self.factoryManagerFullName


class Equip(models.Model):
    equipName = models.CharField(max_length=50)
    # equipType = models.CharField(max_length=50)
    equipVolt = models.IntegerField(validators=[MaxLengthValidator(6), MinLengthValidator(0)], blank=True, null=True)
    equipNo = models.BigIntegerField(null=True)
    STATUS=(
        ('1', 'new'),('2', 'second-hand')
    )
    equipStatus = models.IntegerField(choices=STATUS)
    Factory = models.ForeignKey(Factories, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self