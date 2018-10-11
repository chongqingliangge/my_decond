import redis,logging


class Config(object):
    DEBUG = True
    SECRET_KEY = 'FHAEORFKAHJ'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/information'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = '6379'
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True
    SECRET_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 8860
    LOG_LEVEL = logging.DEBUG


class DevelopementConfig(Config):
    """开发模式下的配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产模式下的配置"""
    LOG_LEVEL = logging.ERROR
config = {
    "development": DevelopementConfig,
    "production": ProductionConfig
}