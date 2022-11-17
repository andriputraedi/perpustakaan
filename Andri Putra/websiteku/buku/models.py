from django.db import models

# Create your models here.
class kategori(models.Model):
    kategori = models.CharField(max_length=100)

class post(models.Model):
    judul = models.CharField(max_length=255)
    sinopsis = models.TextField()
    kategori = models.ForeignKey(kategori, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.judul