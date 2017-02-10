from django.contrib import admin
from .models import CurrentUser
from .models import Vendor
from .models import Buyer
from .models import TenderInfo
from .models import TenderQuotation
from .models import VendorFeedback

# Register your models here.

admin.site.register(CurrentUser)
admin.site.register(Vendor)
admin.site.register(Buyer)
admin.site.register(TenderInfo)
admin.site.register(TenderQuotation)
admin.site.register(VendorFeedback)
