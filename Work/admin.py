from django.contrib import admin
from Work.models import (work,Userinfo,quanxian)
#from Work.models import (work,Userinfo,quanxian,zhuangtaibiao)
# Register your models here.


admin.site.register(work)
admin.site.register(Userinfo)
admin.site.register(quanxian)
#admin.site.register(zhuangtaibiao)