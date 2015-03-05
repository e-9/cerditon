from django.contrib import admin
from cerdoton_app.models import PigData, PigStatus, PigScore

# Register your models here.
class PigStatusInline(admin.TabularInline):
    model = PigStatus
    extra = 2

class PigScoreInline(admin.TabularInline):
    model = PigScore
    extra = 1

class PigDataAdmin(admin.ModelAdmin):
    inlines = [PigStatusInline, PigScoreInline]

admin.site.register(PigData, PigDataAdmin)
