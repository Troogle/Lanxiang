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


def recalculatematch(modeladmin, request, queryset):
	for set in queryset:
		for round in set.round_set.all():
			score = {1: 0, 2: 0}
			for play in round.play_set.all():
				score[play.team] += play.score
			if score[1] > score[2]:
				Play.objects.filter(round__exact=round, team=1).update(useful=True)
				Play.objects.filter(round__exact=round, team=2).update(useful=False)
			else:
				Play.objects.filter(round__exact=round, team=2).update(useful=True)
				Play.objects.filter(round__exact=round, team=1).update(useful=False)
	checkuser.short_description = "Recalculate selected match point(group)"


class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'checked', 'userType', 'point']
	ordering = ['username']
	actions = [checkuser, recalculatepoint]


class MatchAdmin(admin.ModelAdmin):
	actions = [recalculatematch]


admin.site.register(Match, MatchAdmin)
admin.site.register(MatchUser, UserAdmin)
admin.site.register(Beatmap)
admin.site.register(Play)
admin.site.register(Round)

