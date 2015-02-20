# Create your views here.
from datetime import datetime

from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from .utils import *
from .response import JsonResponse
from .models import *


def home(request):
	return render(request, 'index.html', {})


def rules(request):
	return render(request, 'rules.html', {'option': 0})


def pool(request):
	from collections import OrderedDict

	maplist = []
	timedelta = (datetime.now() - datetime(year=2015, month=2, day=19)).days + 1
	timedelta = min(timedelta, 5)
	for date in range(timedelta, 0, -1):
		if Beatmap.objects.filter(date=date).count() == 0:
			continue
		data = {'date': date, 'maps': OrderedDict()}
		data['maps']['None'] = []
		data['maps']['HD'] = []
		data['maps']['DT'] = []
		data['maps']['HR'] = []
		data['maps']['Free Mod'] = []
		for map in Beatmap.objects.filter(date=date):
			data['maps'][map.mode].append(map)
		maplist.append(data)
	return render(request, 'pool.html', {'option': 1, 'list': maplist})


@login_required
def beatmapedit(request):
	if request.method == 'POST':
		import re
		mapurl = request.POST.get('mapurl')
		mode = request.POST.get('mode')
		date = request.POST.get('date')
		diffid = re.match(r"https?://osu\.ppy\.sh/p/beatmap\?b=(\d+).*", mapurl).expand(r"\1")
		setid, mapname, diffname = getmap(diffid)
		map = Beatmap(diffid=setid, mapname=mapname, diffname=diffname, mode=mode, date=date, maxscore=0)
		map.save()
	return render(request, 'beatmapedit.html', {'option': 1})


def matchlist(request):
	return render(request, 'working.html', {'option': 5})


def matchlistadd(request):
	return render(request, 'matchadd.html', {'option': 5})

def matchlistedit(request):
	return render(request, 'playedit.html', {'option': 5})

def statistics(request):
	user = MatchUser.objects.filter(userType=0)
	return render(request, 'statistics.html', {'option': 2, 'list': user})


def staffs(request):
	user = MatchUser.objects.filter(userType=1)
	return render(request, 'staffs.html', {'option': 3, 'list': user})


def reward(request):
	user = MatchUser.objects.filter(userType=0)
	newUser = user.order_by('point')[0:3]
	return render(request, 'reward.html', {'option': 4, 'list': newUser})


def checkcode(request):
	userid = request.GET.get('id')
	userType = request.GET.get('type')
	if userid:
		osuid, username = convertid(userid)
		if osuid == -1:
			return JsonResponse(code=-1)
		else:
			if MatchUser.objects.filter(osuid__exact=osuid):
				return JsonResponse(code='-1')
			tmp = MatchUser(osuid=osuid, username=username, userType=userType)
			tmp.save()
			return JsonResponse(code=0)
	else:
		return JsonResponse(code=-1)
