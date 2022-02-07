from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=255)
    house = models.IntegerField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    street = models.ForeignKey('Street', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
