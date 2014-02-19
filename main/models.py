from django.db import models

# Create your models here.

#GLOBALS:
SUCCESS = 1
ERR_BAD_CREDENTIALS = -1
ERR_USER_EXISTS = -2
ERR_BAD_USERNAME = -3
ERR_BAD_PASSWORD = -4
MAX_USERNAME_LEN = 128
MAX_PASSWORD_LEN = 128


class UserModelManager(models.Manager):

	def add(self, usr, pswd):
		
		if UserModel.objects.filter(username=usr).exists(): #does it exist?
			return ERR_USER_EXISTS
		

		if len(usr) > MAX_USERNAME_LEN or usr == "": #valid name?
			return ERR_BAD_USERNAME
		

		if len(pswd) > MAX_PASSWORD_LEN:   #valid password?
			return ERR_BAD_PASSWORD
		
		#otherwise, create
		the_user = UserModel(username=usr, password=pswd, login_count=1)
		the_user.save()
		return SUCCESS


	def login(self, usr, pswd):
		try:
			the_user = UserModel.objects.get(username=usr, password = pswd)
			the_user.login_count+=1
			the_user.save()
			return the_user.login_count
		except UserModel.DoesNotExist:   #from http://stackoverflow.com/questions/3090302/in-django-how-do-i-objects-get-but-return-none-when-nothing-is-found
			return ERR_BAD_CREDENTIALS

	
	def TESTAPI_resetFixture(self): #for TESTAPI's reasons
		print ("im in hereerererer!!!!!")
		UserModel.objects.all().delete()
		return SUCCESS

class UserModel(models.Model):
	objects = UserModelManager()
	username = models.CharField(unique= True, max_length=MAX_USERNAME_LEN)
	password = models.CharField(max_length=MAX_PASSWORD_LEN)
	login_count = models.IntegerField(default = 1)