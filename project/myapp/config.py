import os


class Config:
    DEBUG = False
    APP_HOST = os.getenv("APP_HOST", '0.0.0.0')
    APP_PORT = os.getenv('APP_PORT', '8080')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '6543')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASS = os.getenv('DB_PASS', 'postgres')
    DB_URL_FMT = 'postgresql://{user}:{pswd}@{host}:{port}/{db_name}'


class DevelopmentConfig(Config):
    DEBUG = True
    DB_NAME = 'real_estate_dev'
    SQLALCHEMY_DATABASE_URI = Config.DB_URL_FMT.format(user=Config.DB_USER, 
                                                       pswd=Config.DB_PASS, 
                                                       host=Config.DB_HOST, 
                                                       port=Config.DB_PORT, 
                                                       db_name=DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    DB_NAME = 'real_estate_test'
    SQLALCHEMY_DATABASE_URI = Config.DB_URL_FMT.format(user=Config.DB_USER, 
                                                       pswd=Config.DB_PASS, 
                                                       host=Config.DB_HOST, 
                                                       port=Config.DB_PORT, 
                                                       db_name=DB_NAME)
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    DB_NAME = 'real_estate'
    SQLALCHEMY_DATABASE_URI = Config.DB_URL_FMT.format(user=Config.DB_USER, 
                                                       pswd=Config.DB_PASS, 
                                                       host=Config.DB_HOST, 
                                                       port=Config.DB_PORT, 
                                                       db_name=DB_NAME)
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


CONFIG_BY_NAME = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
