from django.contrib import admin
from .models import Post,Category,Comment,Courosel,AboutUs,ReaderList
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Courosel)
admin.site.register(AboutUs)
admin.site.register(ReaderList)