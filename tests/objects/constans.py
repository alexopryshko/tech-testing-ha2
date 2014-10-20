__author__ = 'alexander'

import os


class UserData(object):
    USERNAME = 'tech-testing-ha2-24'
    PASSWORD = os.environ.get('TTHA2PASSWORD', 'Pa$$w0rD-24')
    USER_DOMAIN = '@bk.ru'


class Service(object):
    URL = 'https://target.mail.ru'
    BASE_PATH = ''
    LOGIN_PATH = '/login'
    CREATE_PAGE_PATH = '/ads/create'


class AgeRestrictionsData(object):
    AGE = '16+'


class BannerData(object):
    HEADER = 'Titan'
    TEXT = 'Titan is a 2014 multiplayer first-person shooter video game'
    LINK = 'http://my.mail.ru/apps/ID'
    IMG = '/Users/alexander/Development/tech-testing-selenium/res/banner_img.png'


class CSSSelectors(object):
    AUTH_FORM_LOGIN = '#id_Login'
    AUTH_FORM_PASSWORD = '#id_Password'
    AUTH_FORM_DOMAIN = '#id_Domain'
    AUTH_FORM_SUBMIT = '#gogogo>input'
    TOP_MENU_EMAIL = '#PH_user-email'