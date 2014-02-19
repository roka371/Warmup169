from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, Template, Context

from  main.models import *

from django.views.decorators.csrf import csrf_exempt #all calls in django need csrf, this makes it so we dont need it. It's annoying right now 
#and bad practice but that's fine
from main.tests import allTests
import unittest



import json

#GLOBALS:
SUCCESS = 1
ERR_BAD_CREDENTIALS = -1
ERR_USER_EXISTS = -2
ERR_BAD_USERNAME = -3
ERR_BAD_PASSWORD = -4
MAX_USERNAME_LEN = 128
MAX_PASSWORD_LEN = 128


@csrf_exempt
def show(request):
	context = {
		"hello": "hello"
	}
	return render_to_response('index.html', context, context_instance=RequestContext(request))

@csrf_exempt
def welcome(request, user_id):
	user = UserModel.objects.get(pk = user_id)
	context = {
		"user" : user.username,
		"log_count" : user.login_count,
	}
	return render_to_response("welcome.html", context, context_instance = RequestContext(request))

# Create your views here.
@csrf_exempt
def login(request):
	login_count = UserModel.objects.login(usr = request.POST['user'], pswd = request.POST['password']) #this value also might be negative for errs
	res_to_return = {}
	the_user_id = 0
	if login_count >= SUCCESS:
		res_to_return['login'] = login_count
		res_to_return['errCode'] = 1
		the_user_id = UserModel.objects.get(username=request.POST['user']).id
	else:  
		res_to_return['errCode'] = login_count
	return HttpResponse(str(res_to_return['errCode'])+";"+ str(the_user_id))
	#return render_to_response('index.html', res_to_return, context_instance=RequestContext(request))


@csrf_exempt
def add(request):
	login_count = UserModel.objects.add(usr = request.POST['user'], pswd = request.POST['password'])
	the_user_id = 0
	res_to_return = {}
	if login_count >= SUCCESS:
		res_to_return['errCode'] = 1
		res_to_return['count'] = login_count
		the_user_id = UserModel.objects.get(username = request.POST['user']).id
	else:
		res_to_return['errCode'] = login_count
	return HttpResponse(str(res_to_return['errCode'])+";"+str(the_user_id))


@csrf_exempt
def TESTAPI_resetFixture(request):
	try:
		print ("im in herereree! in views")
		res_to_return = {}
		print("im in here!!!! in in views")
		UserModel.objects.all().delete()
		res_to_return['errCode'] = SUCCESS
		
		return render_to_response('index.html', res_to_return, context_instance=RequestContext(request))	
	except:
		return HttpResponse(status=500)



@csrf_exempt
def test(request):
	try:
		result = StringIO()
		tests = (allTests,)
		res_to_return = {}
		res_to_return['nrFailed']= 0
		res_to_return['totalTests'] = 0
		for t in tests:
			test = unittest.TestLoader().loadTestsFromTestCase(t)
			testresult = unittest.TextTestRunner(stream = result, verbosity=5).run(test)
			res_to_return['nrFailed'] += len(testresult.failures)
			res_to_return['totalTests'] += testresult.testsRun
		res_to_return['output'] = result.getValue()
		return render_to_response('index.html', res_to_return, context_instance=RequestContext(request))
	except:
		return HttpResponse(status=200)



