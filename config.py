class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username="kquach",
        password="antiox1234",
        hostname="kquach.mysql.eu.pythonanywhere-services.com",
        databasename="flgaz",
    )
    SQLALCHEMY_USERNAME = 'kquach'
    SQLALCHEMY_PASSWORD = 'antiox1234'
    SQLALCHEMY_DATABASE_NAME = 'kquach$flgaz'


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/flgaz'
    SQLALCHEMY_USERNAME = 'root'
    SQLALCHEMY_PASSWORD = 'password'
    SQLALCHEMY_DATABASE_NAME = 'flgaz'


DEBUG = True


class TestingConfig(Config):
    TESTING = True
