from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Amount(models.Model):
    amount = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return f"ksh {self.amount}"
    
class Payment(models.Model):
    phonenumber = models.CharField(max_length = 12)
    checkoutrequestid = models.CharField(unique= True)
    amountpaid = models.IntegerField()
    confirmed = models.BooleanField(default=False)
    voucher = models.ForeignKey('Voucher', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.checkoutrequestid
    
class Voucher(models.Model):
    code = models.CharField(unique=True, max_length= 6)
    duration = models.ForeignKey(Amount, on_delete=models.CASCADE)
    is_expired = models.BooleanField(default = False)
    valid_until = models.DateTimeField(null = True, blank= True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.valid_until = timezone.now() + timedelta(minutes=self.duration.duration)
        super().save(*args, **kwargs)

    def has_expired(self):
        if self.valid_until:
            return timezone.now() > self.valid_until
        return True

    
