# Create your views here.
from datetime import datetime
import re
from collections import OrderedDict

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404

from .utils import *
from .response import JsonResponse
from .models import *


def home(request):
	return render(request, 'index.html', {})


def rules(request):
	return render(request, 'rules.html', {'option': 0})


def pool(request):
	maplist = []
	timedelta = (datetime.now() - datetime(year=2015, month=2, day=19)).days
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
		mapurl = request.POST.get('mapurl')
		mode = request.POST.get('mode')
		date = request.POST.get('date')
		diffid = re.match(r"https?://osu\.ppy\.sh/p/beatmap\?b=(\d+).*", mapurl).expand(r"\1")
		setid, mapname, diffname = getmap(diffid)
		Beatmap.objects.create(
			diffid=diffid,
			setid=setid,
			mapname=mapname,
			diffname=diffname,
			mode=mode,
			date=date,
			maxscore=0
		)
	return render(request, 'beatmapedit.html', {'option': 1})


def matchlist(request):
	match = Match.objects.all()
	return render(request, 'matchlist.html', {'option': 5, 'list': match})


def matchlistadd(request):
	if request.method == 'POST':
		matchurl = request.POST.get('matchurl')
		date = request.POST.get('date')
		time = request.POST.get('time')
		mpid = re.match(r"https?://osu\.ppy\.sh/mp/(\d+)", matchurl).expand(r"\1")
		match = Match.objects.create(mpid=mpid, date=date, time=time)
		addmatch(mpid, match)
		for user in MatchUser.objects.all():
			user.calculatepoint(date)
		return redirect('ctb.views.matchlistedit', match_id=match.id)
	return render(request, 'matchadd.html', {'option': 5})


def matchlistedit(request, match_id):
	match = get_object_or_404(Match, id=match_id)
	return render(request, 'matchedit.html', {'option': 5, 'match': match})


def playedit(request, play_id):
	play = get_object_or_404(Play, id=play_id)
	if request.method == 'POST':
		playername = request.POST.get('player')
		score = request.POST.get('score')
		failed = True if request.POST.get('failed') else False
		play.player.calculatepoint(play.round.match.date)
		play.score = score
		play.failed = failed
		play.player = MatchUser.objects.get(username=playername)
		play.player.calculatepoint(play.round.match.date)
		play.save()
		return redirect('ctb.views.matchlistedit', match_id=play.round.match.id)
	players = MatchUser.objects.all()
	return render(request, 'playedit.html', {'option': 5, 'play': play, 'players': players})


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
			MatchUser.objects.create(osuid=osuid, username=username, userType=userType)
			return JsonResponse(code=0)
	else:
		return JsonResponse(code=-1)
