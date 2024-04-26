from django.contrib import admin
from importantcontacts.models import MohaPhoneDirectoryList, ProvinceWiseFocalPersonContactList, DeocHeadList, LocalDisasterManagementContactList, MohaSubordinateList


admin.site.register(MohaPhoneDirectoryList)
admin.site.register(ProvinceWiseFocalPersonContactList)
admin.site.register(DeocHeadList)
admin.site.register(LocalDisasterManagementContactList)
admin.site.register(MohaSubordinateList)
