# Create your views here.
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
	user= MatchUser.objects.filter(userType=0)
	return render(request, 'statistics.html', {'option': 2,'list':user})


def staffs(request):
	user= MatchUser.objects.filter(userType=1)
	return render(request, 'staffs.html', {'option': 3,'list':user})

def reward(request):
	user= MatchUser.objects.filter(userType=0)
	newUser= user.order_by('point')[0:3]
	return render(request, 'reward.html', {'option': 4, 'list':newUser})


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
