from django.db import models
from django.db.models import Max
# Create your models here.


# class centroid(models.Model):
#     id = models.AutoField(primary_key=True)
#     type = models.CharField(max_length=100)
#     centroid = models.PointField()

#     def __str__(self):
#         return self.id


class Province(models.Model):
    id = models.AutoField(primary_key=True)
    # bbox = models.PolygonField()
    # centroid = models.ForeignKey(centroid, on_delete=models.CASCADE)
    province_name = models.CharField(max_length=100)
    province_name_ne = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.province_name


class District(models.Model):
    id = models.AutoField(primary_key=True)
    # bbox = models.PolygonField()
    # centroid = models.ForeignKey(centroid, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=100)
    district_name_ne = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.district_name


class Municipality(models.Model):

    id = models.AutoField(primary_key=True)
    # bbox = models.PolygonField()
    # centroid = models.ForeignKey(centroid, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    municipality_name = models.CharField(max_length=100)
    municipality_name_ne = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.municipality_name

    def save(self, *args, **kwargs):
        if not self.id:
            max_id = type(self).objects.filter(
                district=self.district).aggregate(Max('id'))['id__max']
            next_id = (self.district_id * 1000) + \
                1 if max_id is None else max_id + 1
            self.id = next_id
        super().save(*args, **kwargs)


class Ward(models.Model):
    id = models.AutoField(primary_key=True)
   # bbox = models.PolygonField()
    # centroid = models.ForeignKey(centroid, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    ward_name = models.CharField(max_length=100)
    ward_name_ne = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.ward_name

    def save(self, *args, **kwargs):
        if not self.id:
            max_id = type(self).objects.filter(
                district=self.district).aggregate(Max('id'))['id__max']
            next_id = (self.district_id * 100) + \
                1 if max_id is None else max_id + 1
            self.id = next_id
        super().save(*args, **kwargs)
