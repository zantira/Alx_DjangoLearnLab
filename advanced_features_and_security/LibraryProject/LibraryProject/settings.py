"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$1sc7qj^pxtwe7*$kg7ikp1@6(4jmbchl+f9=hlo%)&t#e$+13'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Security settings for browsers
SECURE_BROWSER_XSS_FILTER =     True

X_FRAME_OPTIONS = 'DENY'

SECURE_CONTENT_TYPE_NOSNIFF =    True

# Enforeced cookies to be sent only over HTTPS
CSRF_COOKIE_SECURE = True

# Enforced HTTPS-ONLY cookies
SESSION_COOKIE_SECURE = True

# Configure Application Settings to support and enforced HTTPS

# Set to redirect all non-HTTPS requests to HTTPS
SECURE_SSL_REDIRECT = True

# Instruct browsers to access site only via  HTTPS for one_year
SECURE_HSTS_SECONDS = 315336000

# Include all subdomains in HSTS policy and to allow preloading
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD            = True

# Implement HTTP headers to secure app from attaacks




ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app',
]

# add csp to installed apps

INSTALLED_APPS += ['csp']

CSP_DEFAULT_SRC = ["'self'"]
CSP_SCRIPT_SRC = ["'self'", 'https://trustedscripts.example.com']
CSP_STYLE_SRC = ["'self'", 'https://trustedstyles.example.com']
CSP_IMG_SRC = ["'self'", 'https://trustedimages.example.com']


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# Add django_csp.middleware.CSPMiddleware to MIDDLEWARE.
MIDDLEWARE += ['csp.middleware.CSPMiddleware']

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'bookshelf.CustomUser'