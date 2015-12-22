"""
Django settings for Wysely project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), ".."),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ax@e54crmif^1ul_&4a=c05@it#ug%j04gzm&p%j=brj^5l-z6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['*']

SECRET_KEY = '_'

SITE_ID = 1


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'pipeline',
    'invoices',
    'products',
    'users',
    'customers',
    'companies',
    'contacts',
    'invoicetemplates',
    'common.apps.CommonConfig',
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
)

ROOT_URLCONF = 'wysely.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'wysely.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {}

FIXTURE_DIRS = {
    'fixtures/'
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'staticfiles')
STATIC_ROOT = 'static'

STATIC_URL = '/static/'
 
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
    'pipeline.finders.CachedFileFinder',
)


PIPELINE_CSS = {
    # Project libraries.
    'common_styles': {
        'source_filenames': (
            'css/custom-bootstrap.css',
            'css/main.css',
            'bower_components/gridster/dist/jquery.gridster.min.css',
            'bower_components/js-grid/dist/jsgrid.min.css',
            'bower_components/js-grid/dist/jsgrid-theme.min.css',
            # components
            'css/components/sortable_list.css'
        ),
        # Compress passed libraries and have
        # the output in`css/common_styles.css`.
        'output_filename': 'css/common_styles.css',
    }
}
# JavaScript files.
PIPELINE_JS = {
    # Project JavaScript libraries.
    'common_scripts': {
        'source_filenames': (
            'bower_components/jquery/dist/jquery.js',
            'bower_components/bootstrap/dist/js/bootstrap.js',
            'bower_components/jquery-ui/jquery-ui.min.js',
            'bower_components/ckeditor/ckeditor.js',
            'wysely/site.js',
            'bower_components/gridster/dist/jquery.gridster.min.js',
            'bower_components/js-grid/dist/jsgrid.min.js',
            # components
            'js/navbar_products.js',
            'js/navbar_customers.js',
        ),
        # Compress all passed files into `js/common_scripts.js`.
        'output_filename': 'js/common_scripts.js',
    },

    'products_scripts': {
        'source_filenames': (
            'wysely/products.js',
        ),
        'output_filename': 'js/products_scripts.js',
    }
}

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'


ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_EMAIL_SUBJECT_PREFIX = '[Wysely registration succeeded]'
SEND_ACTIVATION_EMAIL = True
REGISTRATION_AUTO_LOGIN = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTH_PROFILE_MODULE = 'wysely.User'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

try:
    from .local_settings import *
except Exception as e:
    print (e)

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)
PATH_TO_HERE = os.getcwd()
# If we are on heroku we want to re-define the location of the less binary.
HEROKU_LESSC = os.path.join(PATH_TO_HERE, 'lib/node_modules/less/bin/lessc')
HEROKU_NODE = os.path.join(PATH_TO_HERE, 'bin/node')
if os.path.exists(HEROKU_LESSC):
    PIPELINE_LESS_BINARY = "{0} {1}".format(HEROKU_NODE, HEROKU_LESSC)

PIPELINE_LESS_ARGUMENTS = '--include-path=' + ':'.join('{0}/{1}/static/less'.format(PATH_TO_HERE, app) for app in INSTALLED_APPS if app in os.listdir(PATH_TO_HERE))
