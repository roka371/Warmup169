import unittest 
import os
import testLib

SUCCESS = 1
ERR_BAD_CREDENTIALS = -1 
ERR_USER_EXISTS = -2
ERR_BAD_USERNAME = -3
ERR_BAD_PASSWORD = -4
MAX_USERNAME_LENGTH = 128
MAX_PASSWORD_LENGTH = 128

class AllTests(testLib.RestTestCase):

	longstring = "sflvbslkjbvkjefvkehvlfvjkerbfvkjwbevfbehbvliwebrvejvbevwlevkweklrrewfrwebiuewbrivebwrivebirvbewirvbwejhrbvwerbiwerfiwebriuenvihebvoebviwebvjbeijvnwerhvbewjvbeivbiwebveiurbve"

    def test_add_success(self):
        data = { 
            'user' : 'user1',
            'password' : 'pass1',
        }
        respData = self.makeRequest("/users/add", method="POST", data = data)
        self.assertTrue('errCode' in respData)
        self.assertEqual(respData['errCode'], SUCCESS)
        self.assertTrue('count' in respData)
        self.assertEqual(respData['count'], 1)

    
    def test_long_user(self):
        data = {
            'user' : longstring,
            'password' : 'password',
        }
        respData = self.makeRequest("/users/add", method="POST", data = data)
        self.assertTrue('errCode' in respData)
        self.assertEqual(respData['errCode'], ERR_BAD_USERNAME)
        self.assertTrue('count' not in respData)        

    def test_empty_user(self):
        data = {
            'user' : '',
            'password' : 'pass1',
        }
        respData = self.makeRequest("/users/add", method="POST", data = data)
        self.assertTrue('errCode' in respData)
        self.assertEqual(respData['errCode'], ERR_BAD_USERNAME)
        self.assertTrue('count' not in respData)


    def test_long_password(self):
        data = {
            'user' : 'user2',
            'password' : longstring,
        }
        respData = self.makeRequest("/users/add", method="POST", data = data)
        self.assertTrue('errCode' in respData)
        self.assertEqual(respData['errCode'], ERR_BAD_PASSWORD)
        self.assertTrue('count' not in respData)        

    def test_existing_add(self):
        data = { 
            'user' : 'user1',
            'password' : 'password',
        }
        respData = self.makeRequest("/users/add", method="POST", data = data)
        respData = self.makeRequest("/users/add", method="POST", data = data)
        self.assertTrue('errCode' in respData)       
        self.assertEqual(respData['errCode'], ERR_USER_EXISTS)
        self.assertTrue('count' not in respData)


    def test_login(self):
        data = { 
            'user' : 'user1',
            'password' : 'pass1',
        }
        # Create the user
        respData = self.makeRequest("/users/add", method="POST", data = data)
        # Login
        respData = self.makeRequest("/users/login", method="POST", data = data)
        self.assertTrue('errCode' in respData)
        self.assertEqual(respData['errCode'], SUCCESS)
        self.assertTrue('count' in respData)
        self.assertEqual(respData['count'], 2)        
        respData = self.makeRequest("/users/login", method="POST", data = data)
        self.assertTrue('errCode' in respData)
        self.assertEqual(respData['errCode'], SUCCESS)
        self.assertTrue('count' in respData)
        self.assertEqual(respData['count'], 3)

    def test_bad_login(self):
        data = {
            'user' : 'user1',
            'password' : 'wrongpassword',
        }   
        respData = self.makeRequest("/users/login", method="POST", data = data)
        self.assertTrue('errCode' in respData)
        self.assertEqual(respData['errCode'], ERR_BAD_CREDENTIALS)
        self.assertTrue('count' not in respData)