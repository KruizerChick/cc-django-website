"""
Base Django settings project generated using Django 2.2.9.
"""

import os
# Use .env file for environmental and universal settings
from dotenv import load_dotenv

from pathlib import Path  # python3 only
# env_path = Path('.') / '.env'

# load_dotenv(dotenv_path=env_path)


# GENERAL
# -----------------------------------------------------------------------------
SITE_ID = 1

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# URLS and PATHS
# -----------------------------------------------------------------------------
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))
APPS_DIR = os.path.join(BASE_DIR, 'app')
TEMPLATE_DIR = os.path.join(APPS_DIR, 'templates')

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'


# STATIC FILES (CSS, JavaScript, Images)
# --------------------------------------
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = '/static/'
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA FILES
# --------------------------------------
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

# FIXTURES FILES
# --------------------------------------
FIXTURE_DIRS = (os.path.join(BASE_DIR, "fixtures"), )


# APPLICATIONS
# -----------------------------------------------------------------------------

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
    # "django.contrib.admindocs",
]

THIRD_PARTY_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',

]

LOCAL_APPS = [
    'app.users.apps.UsersConfig',
    'app.core.apps.CoreConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE
# -----------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# TEMPLATES
# -----------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
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


# PASSWORDS
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
LOGIN_URL = "account_login"
# LOGIN_REDIRECT_URL = "users:redirect"
LOGIN_REDIRECT_URL = "/"
LOGOUT_URL = 'account_logout'
LOGOUT_REDIRECT_URL = '/'


# THIRD-PARTY SETTINGS
# =============================================================================

# allauth
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS += [
    "allauth.account.auth_backends.AuthenticationBackend",
]
# User's email is required when signing up.
ACCOUNT_EMAIL_REQUIRED=True
# User is blocked from signing in until email is confirmed. 
# ("optional" or "none" allows activity without confirmation)
ACCOUNT_EMAIL_VERIFICATION="optional"
ACCOUNT_PRESERVE_USERNAME_CASING=False
# Don't ask "Remember me?" on log in page.
ACCOUNT_SESSION_REMEMBER=False
# Authenticate by "username", "email" or either "username_email"
ACCOUNT_AUTHENTICATION_METHOD="username_email"

# Django REST Framework
# -----------------------------------------------------------------------------
# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }
