from instance import config


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True


DEBUG = True


class TestingConfig(Config):
    TESTING = True
