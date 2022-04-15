import os


class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class HerokuConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://dvnztlzkcugedp:633bd0a2c7778' \
                              '4971d06e43a30da25c1292de2056b6de5bd9fe292' \
                              '92cf091029@ec2-52-203-118-49.compute-1' \
                              '.amazonaws.com:5432/ddp8i0qsnelnf5'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/sqlite.db'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:pass@127.0.0.1/montreal'
