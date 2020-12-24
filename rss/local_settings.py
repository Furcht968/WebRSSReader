import os

#settings.pyからそのままコピー
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '4n4_fov9g5dxjv!b4!2lq4nuayfofeud3z0^0-9##92lr)n-_*' #追加


#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True #ローカルでDebugできるようになります