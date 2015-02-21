import sys
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

HERE = os.path.dirname(os.path.abspath(__file__))

MANAGERS = ADMINS = ()

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': 'data.db',
	}
}

ALLOWED_HOSTS = ["*"]

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'en-us'

USE_I18N = False

USE_L10N = True

USE_TZ = True

STATIC_ROOT = ''

STATIC_URL = '/static/'

STATICFILES_DIRS = (
	os.path.join(HERE, '../../static'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!dde!5s43g5a8g209p8h94$f#1n$svhti(4tcmj%)i_#pyywb^'

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'settings.urls'

WSGI_APPLICATION = 'settings.wsgi.application'

TEMPLATE_DIRS = (
	os.path.join(HERE, '../../templates'),
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',
	'south',
	'ctb',
)

if os.path.exists(os.path.join(HERE, "local_settings.py")):
	sys.path.append(HERE)
	from local_settings import *