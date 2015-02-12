from django.contrib import admin
from .models import MatchUser
from .models import Match
from .models import Beatmap

# Register your models here.
def checkuser(modeladmin, request, queryset):
    queryset.update(checked=True)
    checkuser.short_description = "Mark selected user checked"

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'checked','userType']
    ordering = ['username']
    actions = [checkuser]

admin.site.register(Match)
admin.site.register(MatchUser,UserAdmin)
admin.site.register(Beatmap)

