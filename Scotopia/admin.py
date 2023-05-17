from django.contrib import admin
from .models import Scotops,Tags,Comments,Category,User
# Register your models here.
admin.site.register(Scotops)
admin.site.register(Tags)
admin.site.register(Comments)
admin.site.register(Category)
admin.site.register(User)