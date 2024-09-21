import os

class Config:
    SECRET_KEY = '241e17c177ec3d4dfa22a3a59ec6d4dd' ##move them to environment variable
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  ##move them to environment variable
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')  ##Email
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')  ##password