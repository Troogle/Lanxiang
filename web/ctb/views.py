﻿# Create your views here.
from django.shortcuts import render
from .utils import convertid
from .response import JsonResponse
from .models import *


def home(request):
	return render(request, 'index.html', {})


def rules(request):
	return render(request, 'rules.html', {'option': 0})


def pool(request):
	return render(request, 'pool.html', {'option': 1})


def statistics(request):
	user= MatchUser.objects.all()
	return render(request, 'statistics.html', {'option': 2,'list':user})


def staffs(request):
	return render(request, 'working.html', {'option': 3})


def support(request):
	return render(request, 'working.html', {'option': 4})


def checkcode(request):
	userid = request.GET.get('id')
	if userid:
		osuid, username = convertid(userid)
		if osuid == -1:
			return JsonResponse(code=-1)
		else:
			if MatchUser.objects.filter(osuid__exact=osuid):
				return JsonResponse(code='-1')
			tmp = MatchUser(osuid=osuid, username=username)
			tmp.save()
			return JsonResponse(code=0)
	else:
		return JsonResponse(code=-1)
