# from django.contrib import admin
# from TestModel.models import Test,Contact,Tag
#
# # Register your models here.
# admin.site.register([Test, Contact, Tag])
#
#


from django.contrib import admin
from TestModel.models import Test, Contact, Tag

# # Register your models here.
# class ContactAdmin(admin.ModelAdmin):
#     fields = ('name', 'email','age')

class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])