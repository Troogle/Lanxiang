from hashlib import sha1 as sha_constructor
import random
import json


try:
	from urllib import request as curl

except ImportError:
	import urllib as curl

KEY = "69dd940656e10cfd73627625cb5a07bea5d2544b"


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