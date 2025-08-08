from django.contrib import admin
from .models import Amount,Payment, Voucher
# Register your models here.
admin.site.register(Amount)
admin.site.register(Payment)
admin.site.register(Voucher)