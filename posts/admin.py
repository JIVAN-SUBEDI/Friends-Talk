from django.contrib import admin
from .models import feeling,activity,sub_activity

# Register your models here.
admin.site.register(feeling)
class SubActivityInline(admin.TabularInline):
    model = sub_activity
    extra = 1  # Number of empty forms to display for adding new SubActivities

class ActivityAdmin(admin.ModelAdmin):
    inlines = [SubActivityInline]

admin.site.register(activity, ActivityAdmin)