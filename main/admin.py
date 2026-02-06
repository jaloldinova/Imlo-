from django.contrib import admin

from main.models import Togri,Notogri

class NotogriInline(admin.StackedInline):
    model = Notogri
    extra = 1

class TogriAdmin(admin.ModelAdmin):
    inlines = [NotogriInline]

admin.site.register(Togri, TogriAdmin)
admin.site.register(Notogri)
