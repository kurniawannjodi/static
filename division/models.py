from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class ContactUs(models.Model):
    nama = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    no_telepon = models.CharField(max_length=30)
    subyek = models.CharField(max_length= 200)
    pesan = models.TextField()
    waktu = models.DateTimeField(auto_now_add=timezone.now())

    def __str__(self):
        return 'Pesan dari {} dengan Subyek {}'.format(self.nama, self.subyek)
