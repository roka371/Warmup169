from django.test import TestCase
import main.models
# Create your tests here.

SUCCESS = 1
ERR_BAD_CREDENTIALS = -1 
ERR_USER_EXISTS = -2
ERR_BAD_USERNAME = -3
ERR_BAD_PASSWORD = -4
MAX_USERNAME_LENGTH = 128
MAX_PASSWORD_LENGTH = 128

class allTests(TestCase):
	very_long_string = "fddfvkjdnkvjdnlbnvslkjfvklsjbvkldjsfvkldfjsbvkljbdsjvsdkjfvskjldbvkjbdvkdjnfvkjdnvkjdfbvjksbfvbjksdvjbsdbdfkbdkvjskdjbvksdjbfvjksdbvklsdjbfvkldsjfbvksdjbfvksdjfbvkjdsfbvklsdjbfvkjbdskbjvsdkljfvksdjbfvksdbfvkjsbdfklvjbsekjvbdkjhsvkljbvksdjbvsdhbvsjdhbvkshdbvjshdbvjsdhbvdsjhbvdsjlhbvdsjbhvdsjbhvdsjhvbdkshbvjs"
	def test_normal_add():
		the_user = UserModel.objects.add(user="user1", password="pass1")
		self.assertEqual(the_user, SUCCESS)
		self.assertEqual(the_user, 1)
	def test_empty_add():
		the_user = UserModel.objects.add(user="", password="pass2")
		self.assertEqual(the_user, ERR_BAD_USERNAME)
	def test_long_user_add():
		the_user = UserModel.objects.add(user=very_long_string, password="pass3")
		self.assertEqual(the_user, ERR_BAD_USERNAME)
	def test_long_pass_add():
		the_user = UserModel.objects.add(user="user2", password=very_long_string)
		self.assertEqual(the_user, ERR_BAD_PASSWORD)

	def test_existing_user():
		the_user = UserModel.objects.add(user="user1", password="pass1")
		self.assertEqual(the_user, ERR_USER_EXISTS)

	def test_login():
		the_user = UserModel.objects.add(user="user3", password="pass3")
		self.assertEqual(the_user, SUCCESS)

		the_user= UserModel.objects.add(user="user3", password="pass3")
		self.assertEqual(the_user, 2)
	def reset():
		self.assertEqual(UserModel.objects.reset(), 1)