from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post,Category,Comment,Courosel,AboutUs,ReaderList

#group
admin.site.unregister(Group)

#sitedecorators
admin.site.site_header = 'TurnOffHumanity'
admin.site.site_title = 'Admin Dashboard'
admin.site.index_title = 'Admin Dashboard'
admin.empty_value_display = '**Empty**'



class PostAdmin(admin.ModelAdmin):
    search_fields = ['Title']
    list_filter = ['Category','DateAdded','Views','Likes']
    list_display = ['Title','Author']

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['Name']
    list_filter = ['Name']

class ReaderListAdmin(admin.ModelAdmin):
    search_fields = ['Email']

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Courosel)
admin.site.register(AboutUs)
admin.site.register(ReaderList,ReaderListAdmin)
