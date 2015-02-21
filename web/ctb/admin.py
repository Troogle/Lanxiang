from django.contrib import admin

from .models import *


# Register your models here.
def checkuser(modeladmin, request, queryset):
	queryset.update(checked=True)
	checkuser.short_description = "Mark selected user checked"


def recalculatepoint(modeladmin, request, queryset):
	for set in queryset:
		for day in range(1, 4):
			set.calculatepoint(day)
	checkuser.short_description = "Recalculate selected user point"


class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'checked', 'userType', 'point']
	ordering = ['username']
	actions = [checkuser, recalculatepoint]


admin.site.register(Match)
admin.site.register(MatchUser, UserAdmin)
admin.site.register(Beatmap)
admin.site.register(Play)
admin.site.register(Round)

