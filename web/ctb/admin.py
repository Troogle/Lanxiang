from django.contrib import admin
from .models import MatchUser
from .models import Match
from .models import Beatmap

# Register your models here.

admin.site.register(Match)
admin.site.register(MatchUser)
admin.site.register(Beatmap)