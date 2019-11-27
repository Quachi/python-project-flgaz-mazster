class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    MYSQL_DATABASE_HOST = 'kquach.mysql.eu.pythonanywhere-services.com'
    MYSQL_DATABASE_USER = 'kquach'
    MYSQL_DATABASE_PASSWORD = 'antiox1234'
    MYSQL_DATABASE_DB = 'kquach$flgaz'


class DevelopmentConfig(Config):
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'password'
    MYSQL_DATABASE_DB = 'flgaz'


DEBUG = True


class TestingConfig(Config):
    TESTING = True
