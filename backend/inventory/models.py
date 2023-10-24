from django.db import models

# Create your models here.
class PlantationWarehouseRow(models.Model):
    row = models.CharField(max_length=50)

    def __str__(self):
        return self.row

class PlantationWareHouseColumn(models.Model):
    row = models.ForeignKey(PlantationWarehouseRow, on_delete=models.PROTECT, related_name="shelfs")
    shelf = models.CharField(max_length=50)

    def __str__(self):
        return f"Row: {self.row.row} Shelf: {self.shelf}"
    
class PlantationWareHouse(models.Model):
    shelf = models.IntegerField()
    row = models.IntegerField()

    # def save(self, *args, **kwargs):
    #     return super(PlantationWareHouse, self).save(args, kwargs)

    def __str__(self):
        return f"Row: {self.row} Shelf: {self.shelf}"