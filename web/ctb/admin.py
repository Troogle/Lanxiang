from django.contrib import admin
from .models import *

# Register your models here.
def checkuser(modeladmin, request, queryset):
    queryset.update(checked=True)
    checkuser.short_description = "Mark selected user checked"

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'checked','userType']
    ordering = ['username']
    actions = [checkuser]

admin.site.register(Match)
admin.site.register(MatchUser, UserAdmin)
admin.site.register(Beatmap)
admin.site.register(Play)
admin.site.register(Round)

