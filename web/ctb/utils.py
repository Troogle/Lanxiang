from hashlib import sha1 as sha_constructor
import random, json

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
		return content[0].get('user_id')
	else:
		return -1