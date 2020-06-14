from django.contrib import admin

from .models import users, todoitems

admin.site.register(users)
admin.site.register(todoitems)


# Register your models here.
