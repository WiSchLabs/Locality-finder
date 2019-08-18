from .base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!X#*zx@k51vg+_M[i8-#SxVcIT6qy]F0kL,95l`M|zS5tF#_JzB-M<qr"V;C3^9c'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'docker',
        'USER': 'docker',
        'PASSWORD': 'docker',
        'HOST': 'postgis-service',
        'PORT': 5432,
    }
}