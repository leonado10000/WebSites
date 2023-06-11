from django.contrib import admin
from .models import Tags,Comment,Category,Persona,Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Persona)