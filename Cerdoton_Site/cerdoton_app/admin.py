from django.contrib import admin
from cerdoton_app.models import PigData, PigStatus

# Register your models here.
class PigStatusInline(admin.TabularInline):
    model = PigStatus
    extra = 2

class PigDataAdmin(admin.ModelAdmin):
    inlines = [PigStatusInline]

admin.site.register(PigData, PigDataAdmin)
