from django.db import models

# Create your models here.
class Pesawat(models.Model):
  nama_pesawat = models.CharField(max_length=255)
  jenis_pesawat = models.CharField(max_length=255)

class Pilot(models.Model):
  nama_pilot = models.CharField(max_length=255)
  nomor_telepon = models.CharField(max_length=255)

class Maskapai(models.Model):
  nama_maskapai = models.CharField(max_length=255)
  lokasi_maskapai = models.CharField(max_length=255)

class Bandara(models.Model):
  nama_bandara = models.CharField(max_length=255)
  lokasi_bandara = models.CharField(max_length=255)
  maskapai = models.ForeignKey(Maskapai, on_delete=models.CASCADE)
  pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
  pesawat = models.ForeignKey(Pesawat, on_delete=models.CASCADE)
  harga_tiket = models.IntegerField()
  jalur = models.CharField(max_length=255)

  
