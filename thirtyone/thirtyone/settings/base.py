from pathlib import Path
import os
import json
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# secrets.json 파일에서 시크릿 키 값 로드하기
secret_file = BASE_DIR / 'secrets.json'

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured(f'Set the {setting} environment variable')

# 시크릿키와 가져오기
SECRET_KEY = get_secret('SECRET_KEY')

# 정적 파일 설정
STATIC_URL = '/static/'

# 사진들 저장을 위한 미디어 경로 설정
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# debug 파일에 있는 관계로 주석 처리
# DEBUG = True

# ALLOWED_HOSTS = [] 

# Application definition

INSTALLED_APPS = [
    #myapps
    'store',
    'buyer',
    'map',
    'dashboard',
    'user',
    #basic apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #external apps
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'drf_yasg',
    'django_celery_beat', # 30분후 자동 주문 취소때 쓰임
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # 코스헤더 설정추가
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', csrt주석처리
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

CORS_ALLOW_METHODS = [  # 허용할 옵션
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [  # 허용할 헤더
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ALLOW_CREDENTIALS = True # 쿠키 등의 요청을 허용할지 여부

CORS_ALLOW_ALL_ORIGINS: True #  모든 출저 허용


ROOT_URLCONF = 'thirtyone.urls'

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

WSGI_APPLICATION = 'thirtyone.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# debug 파일에 따로 있음으로 주석처리하였음
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Celery Beat 설정 추가
CELERY_BEAT_SCHEDULE = {
    'check_order_status': {
        'task': 'store.tasks.check_order_status',
        'schedule': 30.0,  # 30초마다 작업 실행
    },
}

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

LANGUAGE_CODE = 'ko-kr' # 언어를 한국어로 변경해줍니다

TIME_ZONE = 'Asia/Seoul' # 시간대를 서울로 변경해줍니다

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
