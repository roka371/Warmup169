

PRODUCTION = True #turn False if on local machine



"""
Django settings for warmup169 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y)ievx&ga)ib8h&vpuyj9i2)6g$!=*84gre^2t_aaw+$*k#j%e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	#custom
	'main',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'warmup169.urls'

WSGI_APPLICATION = 'warmup169.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if(PRODUCTION == True):
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		}
	}

	# Parse database configuration from $DATABASE_URL
	import dj_database_url
	DATABASES['default'] =  dj_database_url.config()


	# Honor the 'X-Forwarded-Proto' header for request.is_secure()
	SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		}
	}

"""
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',       # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'warmup169',                              # Or path to database file if using sqlite3.
		'USER': 'root',                             # Not used with sqlite3.
		'PASSWORD': 'Ego371!FTW',                   # Not used with sqlite3.
		'HOST': '',                                 # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',                                 # Set to empty string for default. Not used with sqlite3.
	}
}"""

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Allow all host headers
ALLOWED_HOSTS = ['*']


# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'static'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)

BASE_REL_PATH = os.path.dirname(os.path.realpath(__file__))

TEMPLATE_DIRS = (os.path.join(BASE_REL_PATH,'templates/'))


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
