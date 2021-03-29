from django.contrib import admin
from .models import Player

# Register your models here.

# 管理画面で表示するcol
class PlayerDirectoryAdmin(admin.ModelAdmin): 
    list_display = ('pos', 'num','age','barth','name')

admin.site.register(Player,PlayerDirectoryAdmin)
