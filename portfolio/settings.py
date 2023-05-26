"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from .local_settings import config
from pathlib import Path
from corsheaders.defaults import default_headers
# from decouple import config

DEBUG = config('DEBUG')
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'contact',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

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

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = config('DATABASES')


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOWED_ORIGINS  = config('CORS_ALLOWED_ORIGINS')
CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ORIGIN_WHITELIST = config('CORS_ORIGIN_WHITELIST')
#CORS_ALLOWED_ORIGIN_REGEXES = [
#    r"^https://\w+\.codedevest\.com$",
#]
#CORS_URLS_REGEX = r"^.*/api/.*$"
#CORS_ALLOW_PRIVATE_NETWORK: True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    # 'PATCH',
    'DELETE',
    # 'OPTIONS',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
    }

# EMAIL_HOST = 'smtp.googlemail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = config('EMAIL_HOST_USER')


# CORS_ALLOW_HEADERS  = list(default_headers) + [ "WWW-Authenticate", "Authorization", "Proxy-Authenticate", "Proxy-Authorization", "Age", "Cache-Control", "Clear-Site-Data", "Expires", "Pragma", "Warning", "Accept-CH", "Accept-CH-Lifetime", "Sec-CH-UA", "Sec-CH-UA-Arch", "Sec-CH-UA-Bitness", "Sec-CH-UA-Full-Version", "Sec-CH-UA-Full-Version-List", "Sec-CH-UA-Mobile", "Sec-CH-UA-Model", "Sec-CH-UA-Platform", "Sec-CH-UA-Platform-Version", "Content-DPR", "Device-Memory", "DPR", "Viewport-Width", "Width", "Downlink", "ECT", "RTT", "Save-Data", "Last-Modified", "ETag", "If-Match", "If-None-Match", "If-Modified-Since", "If-Unmodified-Since", "Vary", "Connection", "Keep-Alive", "Accept", "Accept-Encoding", "Accept-Language", "Expect", "Max-Forwards", "Cookie", "Set-Cookie", "Access-Control-Allow-Origin", "Access-Control-Allow-Credentials", "Access-Control-Allow-Headers", "Access-Control-Allow-Methods", "Access-Control-Expose-Headers", "Access-Control-Max-Age", "Access-Control-Request-Headers", "Access-Control-Request-Method", "Origin", "Timing-Allow-Origin", "Content-Disposition", "Content-Length", "Content-Type", "Content-Encoding", "Content-Language", "Content-Location", "Forwarded",  "X-Forwarded-For", "X-Forwarded-Host", "X-Forwarded-Proto", "Via", "Location", "From", "Host", "Referer", "Referrer-Policy", "User-Agent", "Allow", "Server", "Accept-Ranges", "Range", "If-Range", "Content-Range", "Cross-Origin-Embedder-Policy", "Cross-Origin-Opener-Policy", "Cross-Origin-Resource-Policy", "Content-Security-Policy", "Content-Security-Policy-Report-Only", "Expect-CT", "Feature-Policy", "Origin-Isolation", "Strict-Transport-Security", "Upgrade-Insecure-Requests", "X-Content-Type-Options", "X-Download-Options", "X-Frame-Options", "X-Permitted-Cross-Domain-Policies", "X-Powered-By", "X-XSS-Protection", "Sec-Fetch-Site", "Sec-Fetch-Mode", "Sec-Fetch-User", "Sec-Fetch-Dest", "Service-Worker-Navigation-Preload", "Last-Event-ID", "NEL", "Ping-From", "Ping-To", "Report-To", "Transfer-Encoding", "TE", "Trailer", "Sec-WebSocket-Key", "Sec-WebSocket-Extensions", "Sec-WebSocket-Accept", "Sec-WebSocket-Protocol", "Sec-WebSocket-Version", "Accept-Push-Policy", "Accept-Signature", "Alt-Svc", "Date", "Early-Data", "Large-Allocation", "Link", "Push-Policy", "Retry-After", "Signature", "Signed-Headers", "Server-Timing", "Service-Worker-Allowed", "SourceMap", "Upgrade", "X-DNS-Prefetch-Control", "X-Firefox-Spdy", "X-Pingback", "X-Requested-With", "X-Robots-Tag", "X-UA-Compatible", "ContentType", "Content-type", "content-type", "contenttype", "contentType", "accept", "authorization", "dnt", "origin", "user-agent", "x-csrftoken", "x-requested-with", "accept-encoding", "Contentype"]
