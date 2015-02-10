from django.http import HttpResponse
import json


class JsonResponse(HttpResponse):
	def __init__(self, code=None, data=None):
		ret = {}
		if code:
			ret["code"] = code
		else:
			ret["code"] = 0
		if data:
			ret["data"] = data
		HttpResponse.__init__(self, json.dumps(ret))