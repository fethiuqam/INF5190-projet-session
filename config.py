import os


class Config:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class HerokuConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://lttrqunjwirccz:84a044558cb0d36c' \
                              'ff8188a8b08694d8fd720c4541b98043820ca89a60b' \
                              'b9443@ec2-54-80-123-146.compute-1.' \
                              'amazonaws.com:5432/d6l61vp1vehd4k'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/sqlite.db'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/sqlite.db'
