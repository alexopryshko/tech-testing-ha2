__author__ = 'alexander'

import urlparse
from components import AuthForm, TopMenu, BaseSettings, Banner, AgeRestrictions, Interests, MainButton
from constans import Service


class Page(object):
    BASE_URL = Service.URL
    PATH = Service.BASE_PATH

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)


class AuthPage(Page):
    PATH = Service.LOGIN_PATH

    @property
    def form(self):
        return AuthForm(self.driver)


class CreatePage(Page):
    PATH = Service.CREATE_PAGE_PATH

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def base_settings(self):
        return BaseSettings(self.driver)

    @property
    def banner(self):
        return Banner(self.driver)

    @property
    def age_restrictions(self):
        return AgeRestrictions(self.driver)

    @property
    def interests(self):
        return Interests(self.driver)

    @property
    def main_button(self):
        return MainButton(self.driver)


