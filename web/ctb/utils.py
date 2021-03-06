from collections import OrderedDict
from hashlib import sha1 as sha_constructor
import random
import json

from .models import *


try:
	from urllib import request as curl

except ImportError:
	import urllib as curl

KEY = "69dd940656e10cfd73627625cb5a07bea5d2544b"


def get_object_or_none(model, *args, **kwargs):
	try:
		return model.objects.get(*args, **kwargs)
	except model.DoesNotExist:
		return None


def generate():
	return sha_constructor(str(random.random())).hexdigest()[:8]


def checkcode(code):
	return False


def convertid(osuid):
	raw = ""
	raw = curl.urlopen('http://osu.ppy.sh/api/get_user?k=' + KEY + '&u=' + str(osuid)).read()
	content = json.loads(raw.decode('utf-8'))
	if len(content) != 0:
		return content[0].get('user_id'), content[0].get('username')
	else:
		return -1, ""


def getmap(diffid):
	raw = curl.urlopen('http://osu.ppy.sh/api/get_beatmaps?k=' + KEY + '&b=' + str(diffid)).read()
	content = json.loads(raw.decode('utf-8'))
	if len(content) != 0:
		return content[0].get('beatmapset_id'), \
			   content[0].get('artist') + '-' + content[0].get('title'), \
			   content[0].get('version')
	else:
		return -1, "", ""


def addmatch(mpid, match):
	raw = curl.urlopen('http://osu.ppy.sh/api/get_match?k=' + KEY + '&mp=' + str(mpid)).read()
	content = json.loads(raw.decode('utf-8'))
	if len(content) == 0:
		return
	content = content['games']
	order = 0
	for round in content:
		cmap = get_object_or_none(Beatmap, diffid=round['beatmap_id'])
		if cmap is None:
			continue
		cround = Round.objects.create(match=match, map=cmap, order=order)
		order += 1
		tscore={}
		if round["team_type"] == '2':
			tscore = {u'1': 0, u'2': 0}
		for play in round['scores']:
			cplayer = get_object_or_none(MatchUser, osuid=play['user_id'])
			if cplayer is None:
				continue
			score = play['score']
			team = play['team']
			failed = False if play['pass'] == '1' else True
			cplay = Play.objects.create(player=cplayer, round=cround, score=score, failed=failed, team=team)
			if round["team_type"] == '2':
				tscore[team] += int(score)
		if tscore[u'1'] > tscore[u'2']:
			Play.objects.filter(round__exact=cround, team=1).update(useful=True)
		else:
			Play.objects.filter(round__exact=cround, team=2).update(useful=True)


def PackMapData(date):
	data = {'date': date, 'maps': OrderedDict()}
	if Beatmap.objects.filter(date=date).count() == 0:
		return data
	data['maps']['None'] = []
	data['maps']['HD'] = []
	data['maps']['DT'] = []
	data['maps']['HR'] = []
	data['maps']['Free Mod'] = []
	if Beatmap.objects.filter(date=date, mode="Tie Breaker").count() != 0:
		data['maps']['Tie Breaker'] = []
	for map in Beatmap.objects.filter(date=date):
		data['maps'][map.mode].append(map)
	return data