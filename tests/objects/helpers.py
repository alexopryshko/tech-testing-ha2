__author__ = 'alexander'

from selenium.webdriver.support.wait import WebDriverWait
from constans import WebDriverSettings


def get_element_by_css_selector(driver, css):
    return WebDriverWait(driver, WebDriverSettings.TIMEOUT, WebDriverSettings.POLL_FREQUENCY).until(
        lambda d: d.find_element_by_css_selector(css)
    )


def get_element_by_xpath(driver, xpath):
    return WebDriverWait(driver, WebDriverSettings.TIMEOUT, WebDriverSettings.POLL_FREQUENCY).until(
        lambda d: d.find_element_by_xpath(xpath)
    )

