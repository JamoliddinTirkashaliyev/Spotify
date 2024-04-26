from django.db import models


class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=100)
    tugilgan_yil = models.DateField()
    davlat = models.CharField(max_length=250)


class Albom(models.Model):
    nom = models.CharField(max_length=250)
    sana = models.DateField()
    rasm = models.ImageField(upload_to='albomlar/',blank=True,null=True)
    qoshiqchi = models.ForeignKey(Qoshiqchi,on_delete=models.CASCADE)

class Qoshiq(models.Model):
    nom = models.CharField(max_length=250)
    janr = models.CharField(max_length=50)
    davomiylik = models.DurationField(blank=True,null=True)
    audio = models.FileField(upload_to='qoshiqlar/',blank=True,null=True)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)





