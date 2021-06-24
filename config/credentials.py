"""
"""
SECRET_KEY = '6\xd4\x8e\x1d\xca\x02[\xe8\xf3\xabC\xe1\xe1\xe8&\xb9p\x00\x04U\x16\x7f!\x87'

# Allowed host for CORS 
ALLOWED_HOSTS = []


DATABASES = {
    'development': {
        'MONGODB_DB': 'kumkd',
        'MONGODB_HOST': 'kumkd',
        'MONGODB_PORT': 'celcoevb0312.us.oracle.com',
        'MONGODB_USERNAME': '1522',
        'MONGODB_PASSWORD': ''
    },
    'production': {
        'SERVICE_NAME':'********',
        'USER': '********',
        'PASSWORD': '********',
        'HOST': '********',
        'PORT': '********',
    },
    'testing':{
        'SERVICE_NAME':'********',
        'USER': '********',
        'PASSWORD': '********',
        'HOST': '********',
        'PORT': '********',

    }
}
