import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTH_USER_MODEL = 'testapp.User'



SECRET_KEY = '5#qg!6k$xx)ky7u@)2rex9m5x!io2l#p(0oz$1si29nq!7d@c!'


DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'activity_log',  # LOG
    'testapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'activity_log.middleware.ActivityLogMiddleware',  # LOG
)

ROOT_URLCONF = 'testproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'testproject.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # LOG
    'logs': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'logs.sqlite3'),
    }
}

DATABASE_ROUTERS = ['activity_log.router.DatabaseAppsRouter']  # LOG
DATABASE_APPS_MAPPING = {'activity_log': 'logs'}  # LOG


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'


ACTIVITYLOG_EXCLUDE_URLS = ('/admin/activity_log/activitylog', )
ACTIVITYLOG_EXCLUDE_STATUSES = (302, )
ACTIVITYLOG_METHODS = ('POST', 'GET')
ACTIVITYLOG_LAST_ACTIVITY = True
ACTIVITYLOG_GET_EXTRA_DATA = 'testapp.models.make_extra_data'
