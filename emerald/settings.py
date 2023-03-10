from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-+hs+!rmh=_e#7@5j)1&or10+92ccm&9uez-60b*voj9m-xb#@*'

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios',
    'produtos',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "emerald.middleware.Csrf.CsrfExemptMiddleware",
]

ROOT_URLCONF = 'emerald.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'emerald.contextProcessors.Url.baseUrl',
            ],
        },
    },
]

WSGI_APPLICATION = 'emerald.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = 'usuarios.Cliente'

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

LOGIN_URL = '/auth/login/'

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Caminho que ?? mostrado fora do django (n??o faz diferen??a)
STATIC_URL = 'static/'

# Caminho dos arquivos est??ticos dentro do projeto
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates/static')
]

# Caminho dos arquivos est??ticos da produ????o
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Onde ?? salvo os arquivos de media salvos pelo usu??rio
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Limpa a sess??o quando o browser ?? fechado
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# expira os cookies em uma hora
SESSION_COOKIE_AGE = 3600