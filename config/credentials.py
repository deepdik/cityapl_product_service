"""
"""
SECRET_KEY = '6\xd4\x8e\x1d\xca\x02[\xe8\xf3\xabC\xe1\xe1\xe8&\xb9p\x00\x04U\x16\x7f!\x87'

# Allowed host for CORS 
ALLOWED_HOSTS = []


DATABASES = {
    'mysql_rds': {
        'NAME': 'cityapl',
        'USER': 'admin',
        'PASSWORD': 'cityapl_rds123',
        'HOST': 'cityapl-database-1.cyvpsljpkc8d.ap-south-1.rds.amazonaws.com',
        'PORT': '3306',
        },
    'postgres': {
        'NAME': 'cityapl',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': '13.233.128.251',
        'PORT': '5432'
        },
    'mongo': {
        'MONGODB_DB': '',
        'MONGODB_HOST': '',
        'MONGODB_PORT': '',
        'MONGODB_USERNAME': '',
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

REDIS_CACHE = {
        'CACHE_TYPE':'RedisCache',
        'CACHE_REDIS_HOST':'redis',
        'CACHE_REDIS_PORT': 6379,
        'CACHE_REDIS_DB':0,
        'CACHE_REDIS_URL':'redis://redis:6379/0',
        'CACHE_DEFAULT_TIMEOUT':500
    }


CELERY_BROKER_URL= 'amqp://cityapl-rabbitmq:cityapl@168.138.113.89:5672//'
CELERY_RESULT_BACKEND= 'rpc://'
CELERY_ACKS_LATE = True
