# Create your views here.
from django.shortcuts import render_to_response
def home(request):
    return render_to_response('index.html',{})
def rules(request):
    return render_to_response('working.html',{})
def pool(request):
    return render_to_response('working.html',{})
def statistics(request):
    return render_to_response('working.html',{})
def staffs(request):
    return render_to_response('working.html',{})
def support(request):
    return render_to_response('working.html',{})
def register(request):
    return render_to_response('working.html',{})