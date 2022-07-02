from django.contrib import admin

#from .models import UsersPosts


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'email')


#admin.site.register(UsersPosts)
