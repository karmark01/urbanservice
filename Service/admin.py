from django.contrib import admin
from .models import Uuser,service,category,Requestss,requests
# # Register your models here.

# admin.site.register(service)

@admin.register(Uuser)
class UuserAdmin(admin.ModelAdmin):
    list_display = ['uid','name','profile','lname','email','password','role']


@admin.register(service)
class serviceAdmin(admin.ModelAdmin):
    list_display = ['sid','uid','type','date','Time','address',]

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['cid','cname']


@admin.register(Requestss)
class RequestssAdmin(admin.ModelAdmin):
    list_display = ['req','uid','sid']



@admin.register(requests)
class requestsAdmin(admin.ModelAdmin):
    list_display = ['req','uid','sid']