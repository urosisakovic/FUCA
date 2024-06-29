"""
Author: Djodje Vucinic
"""
import os


class Config:
    """
    Configuration class for Flask app.
    """
    SECRET_KEY = os.environ.get('FUCA_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('FUCA_SQLALCHEMY_DATABASE_URI')

    MAIL_USERNAME = os.environ.get('FUCA_EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('FUCA_EMAIL_PASS')

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
