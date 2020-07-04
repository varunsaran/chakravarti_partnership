from django.contrib import admin
from .models import UserData
from .models import PartnershipData, TransactionHistory, Holdings
# Register your models here.

admin.site.register(UserData)
admin.site.register(PartnershipData)
admin.site.register(TransactionHistory)
admin.site.register(Holdings)
