class Config():
    SECRET_KEY = 'b97a6d5e52eb344c598e743'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'kioskopop'

config = {
    'development': DevelopmentConfig
}
