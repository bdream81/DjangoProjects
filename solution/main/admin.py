from django.contrib import admin

# Register your models here.
from .models import ImgPathSingle, TextSingle, TextSingles, ImgTextGroup, IntCharGroup, CustomersGroup, LogoGroup

admin.site.register(ImgPathSingle)
admin.site.register(TextSingle)
admin.site.register(TextSingles)
admin.site.register(ImgTextGroup)
admin.site.register(IntCharGroup)
admin.site.register(CustomersGroup)
admin.site.register(LogoGroup)