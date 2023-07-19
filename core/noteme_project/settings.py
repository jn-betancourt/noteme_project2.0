from pathlib import Path
import os
import environ
from corsheaders.defaults import default_headers

env = environ.Env()
environ.Env().read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS_DEV")

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "apps.notes.apps.NotesConfig",
    "apps.users.apps.UsersConfig",
    "apps.googleAPI.apps.GoogleapiConfig",
]

THIRD_PARTY_APP = [
    "corsheaders",
    "rest_framework",
    "ckeditor",
    "ckeditor_uploader",
    "rest_framework.authtoken",
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APP

CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "custom",
        "toolbar_Custom": [
            ["Bold", "Italic", "Underline"],
            [
                "NumberedList",
                "BulletedList",
                "-",
                "Outdent",
                "Indent",
                "-",
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
            ],
            ["Link", "Unlink"],
            ["RemoveFormat", "Source"],
        ],
        "autoParagraph": False,
    }
}
CKEDITOR_UPLOAD_PATH = "/media/"

SECURE_CROSS_ORIGIN_OPENER_POLICY = env.get_value("SECURE_CROSS_ORIGIN_OPENER_POLICY")

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "csp.middleware.CSPMiddleware",
    "django_referrer_policy.middleware.ReferrerPolicyMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "noteme_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "build")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "noteme_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "build/static")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWOKR = {
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
}

# REFERRER POLICY
REFERRER_POLICY = os.environ.get("REFERRER_POLICY")

# CSP CONFIG FOR GOOGLE AUTH
CSP_DEFAULT_SRC = env.list("CSP_DEFAULT_SRC")
CSP_CONNECT_SRC = env.list("CSP_CONNECT_SRC")
CSP_STYLE_SRC = env.list("CSP_STYLE_SRC")
CSP_SCRIPT_SRC = env.list("CSP_DEFAULT_SRC")
CSP_FRAME_SRC = env.list("CSP_FRAME_SRC")
CSP_CONNECT_SRC = env.list("CSP_CONNECT_SRC")

# CORS HEADERS AND CRF CONFIG
CORS_ORIGIN_WHITELIST = env.list("CORS_ORIGIN_WHITELIST_DEV")
CORS_ALLOW_HEADERS = (*default_headers, *env.tuple("CORS_ALLOW_HEADERS"))
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS_DEV")

if not DEBUG:
    ALLOWED_HOSTS = env.list("ALLOWED_HOSTS_DEPLOY")
    CORS_ORIGIN_WHITELIST = env.list("CORS_ORIGIN_WHITELIST_DEPLOY")
    CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS_DEPLOY")

    DATABASES = {"default": env.db("DATABASE_URL")}
    DATABASES["default"]["ATOMIC_REQUEST"] = True
