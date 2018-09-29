class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    debug=True

    SQLALCHEMY_DATABASE_URI= "sqlite:///databases.db"
    SQLALCHEMY_ECHO=True
