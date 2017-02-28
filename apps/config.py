import logging
import os
from pymongo.uri_parser import parse_uri


class Config(object):
    def __init__(self):
        self.DEBUG = False
        self.TESTING = False
        self.HEROKU = False
        self.PRODUCTION = False

        self.SECRET_KEY = '{SECRET_KEY}'
        self.SITE_NAME = 'Flask Site'
        self.LOG_LEVEL = logging.DEBUG
        self.SERVER_NAME = 'localhost:5000'

        self.SYS_ADMINS = ['foo@example.com']

#mongodb support
        self.MONGODB_SETTINGS = self.mongo_from_uri(
            'mongodb://localhost:27017/development'
        )

        #Configured for email
        self.DEFAULT_MAIL_SENDER = 'Admin <peng.weilin@yahoo.com >'
        self.MAIL_SERVER = 'smtp.mail.yahoo.com'
        self.MAIL_PORT = 587
        self.MAIL_USE_SSL =True
        self.MAIL_USERNAME = 'peng.weilin@yahoo.com'
        self.MAIL_PASSWORD = '57266713sweet'

        #Flask-Security setup
        self.SECURITY_EMAIL_SENDER = 'Security < peng.weilin@yahoo.com >'
        self.SECURITY_LOGIN_WITHOUT_CONFRMATION = True
        self.SECURITY_REGISTERABLE = True
        self.SECURITY_RECOVERABLE = True
        self.SECURITY_URL_PREFIX = '/auth'
        self.SECURITY_POST_LOGIN = '/'
        self.SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
        #import uuid;salt = uuid.uuid4().hex
        self.SECURITY_PASSWORD_SALT = '2b8b74fc58e489e879810905b6b6d4dc6'

        self.SECURITY_CONFIRMABLE = True
        self.SECURITY_LOGIN_WITHOUT_CONFIRMATION = False

        #CACHE
        self.CACHE_TYPE = 'simple'

    @staticmethod
    def mongo_from_uri(uri):
        config = parse_uri(uri)
        conn_settings = {
            'db':config['database'],
            'username':config['username'],
            'password':config['password'],
            'host':config['nodelist'][0][0],
            'port':config['nodelist'][0][1]
        }
        return conn_settings


class ProductionConfig(Config):
    def __init__(self):
        super(ProductionConfig,self).__init__()
        self.ENVIRONMENT = 'Production'
        self.HEROKU = True
        self.PRODUCTION = True
        self.LOG_LEVEL = logging.INFO
        self.SERVER_NAME = 'example.com'


        self.MONGODB_SETTINGS = self.mongo_from_uri(os.getenv('MONGOHQ_URL'))


class DevelopmentConfig(Config):
    '''
    Use "if app.debug" anywhere in your code,
    that code will run in development mode.
    '''
    def __init__(self):
        super(DevelopmentConfig,self).__init__()
        self.ENVIRONMENT = 'Dev'
        self.DEBUG = True
        self.TESTING = False


class TestingConfig(Config):
    '''
    A Config to use when we are runing tests.
    '''
    def __init__(self):
        super(TestingConfig,self).__init__()
        self.ENVIRONMENT = 'Testing'
        self.DEBUG = False
        self.TESTING = True

        self.MONGDB_SETTINGS = self.mongo_from_uri(
            'mong0db://licalhost:27017/testing'
        )


environment = os.getenv('ENVIRONMENT','DEVELOPMENT').lower()
#Alteenatively this may be easier if you are managing multiple aws servers
#environment = socket.gethostname().lower()

if environment == 'testing':
    app_config = TestingConfig()
elif environment == 'Production':
    app_config = ProductionConfig()
else:
    app_config = DevelopmentConfig()
