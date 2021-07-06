from django.contrib import admin

# Register your models here.
from .models import ImgPathSingle, TextSingle, TextGroup, ImgTextGroup, Group4, LogoGroup

admin.site.register(ImgPathSingle)
admin.site.register(TextSingle)
admin.site.register(TextGroup)
admin.site.register(ImgTextGroup)
admin.site.register(Group4)
admin.site.register(LogoGroup)