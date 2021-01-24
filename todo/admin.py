from django.contrib import admin
from todo.models import Todo



class todoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)



admin.site.register(Todo,todoAdmin)