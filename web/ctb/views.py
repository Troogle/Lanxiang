# Create your views here.
from django.shortcuts import render
from .utils import generate, checkcode, convertid
from .response import JsonResponse
from .models import *

def home(request):
	return render(request, 'index.html', {})


def rules(request):
	return render(request, 'working.html', {})


def pool(request):
	return render(request, 'working.html', {})


def statistics(request):
	return render(request, 'working.html', {})


def staffs(request):
	return render(request, 'working.html', {})


def support(request):
	return render(request, 'working.html', {})


def register(request):
	return render(request, 'register.html', {})


def checkcode(request):
	userid = request.GET.get('id')
	if userid:
		osuid = convertid(userid)
		if osuid == -1:
			return JsonResponse(code=-1)
		else:
			if MatchUser.objects.filter(osuid__exact=osuid):
				return JsonResponse(code='-1')
			tmp = MatchUser(osuid=osuid)
			tmp.save()
			return JsonResponse(code=0)
	else:
		return JsonResponse(code=-1)
