class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class HerokuConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql-reticulated-17362'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/sqlite.db'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/sqlite.db'

