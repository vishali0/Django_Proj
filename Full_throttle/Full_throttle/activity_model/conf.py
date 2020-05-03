
from __future__ import unicode_literals

from django.conf import settings



ANONIMOUS = getattr(settings, 'ACTIVITYLOG_ANONIMOUS', True)


LAST_ACTIVITY = getattr(settings, 'ACTIVITYLOG_LAST_ACTIVITY', True)


METHODS = getattr(settings, 'ACTIVITYLOG_METHODS',
                  ('GET', 'POST', 'PUT', 'PATCH', 'DELETE'))


STATUSES = getattr(settings, 'ACTIVITYLOG_STATUSES', None)


EXCLUDE_STATUSES = getattr(settings, 'ACTIVITYLOG_EXCLUDE_STATUSES', None)


EXCLUDE_URLS = getattr(settings, 'ACTIVITYLOG_EXCLUDE_URLS', ())


AUTOCREATE_DB = getattr(settings, 'ACTIVITYLOG_AUTOCREATE_DB', False)


IP_ADDRESS_HEADERS = ('HTTP_X_REAL_IP', 'HTTP_CLIENT_IP',
                      'HTTP_X_FORWARDED_FOR', 'REMOTE_ADDR')


GET_EXTRA_DATA = getattr(settings, 'ACTIVITYLOG_GET_EXTRA_DATA', None)


LOG_DB_KEY = getattr(settings, 'DATABASE_APPS_MAPPING', {}).get('activity_model')

if LOG_DB_KEY and not settings.DATABASES.get(LOG_DB_KEY):
    db = settings.DATABASES['default'].copy()
    db['NAME'] = '{}_{}'.format(db['NAME'], LOG_DB_KEY)
    settings.DATABASES[LOG_DB_KEY] = db