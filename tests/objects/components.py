# coding=utf-8
__author__ = 'alexander'

from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from constans import CSSSelectors, BannerData, AgeRestrictionsData
from helpers import *


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = CSSSelectors.AUTH_FORM_LOGIN
    PASSWORD = CSSSelectors.AUTH_FORM_PASSWORD
    DOMAIN = CSSSelectors.AUTH_FORM_DOMAIN
    SUBMIT = CSSSelectors.AUTH_FORM_SUBMIT

    def set_login(self, login):
        self.driver.find_element_by_css_selector(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(pwd)

    def set_domain(self, domain):
        select = self.driver.find_element_by_css_selector(self.DOMAIN)
        Select(select).select_by_visible_text(domain)

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()


class TopMenu(Component):
    EMAIL = CSSSelectors.TOP_MENU_EMAIL

    def get_email(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EMAIL).text
        )


class BaseSettings(Component):
    TARGET = '//*[@id="product-type-5208"]'
    PLAYGROUND = '//*[@id="pad-mail_mir_abstract"]'
    CAMPAIGN_NAME = '.base-setting__campaign-name__input'
    CAMPAIGN = 'Infinity of war'

    def set_target(self):
        get_element_by_xpath(self.driver, self.TARGET).click()

    def set_playground(self):
        get_element_by_xpath(self.driver, self.PLAYGROUND).click()

    def set_campaign_name(self):
        campaign_name = get_element_by_css_selector(self.driver, self.CAMPAIGN_NAME)
        campaign_name.clear()
        campaign_name.send_keys(self.CAMPAIGN)


class Banner(Component):
    BANNER_HEADER = '[data-name="title"] .banner-form__input'
    BANNER_TEXT = '[data-name="text"] .banner-form__input_text-area'
    BANNER_LINK = './/li[@data-top="false"]//input[@data-name="url"]'
    BANNER_IMG = '.banner-form__img-file'
    IMG_CROPPER = '.image-cropper__save'
    SAVE_BUTTON = '.banner-form__save-button'

    PREVIEW_BANNER_HEADER = '//ul[@class="added-banner__banners-wrapper"]//span[@class="banner-preview__title"]'
    PREVIEW_BANNER_TEXT = '//ul[@class="added-banner__banners-wrapper"]//p[@class="banner-preview__text"]'

    def set_banner_header(self):
        get_element_by_css_selector(self.driver, self.BANNER_HEADER).send_keys(BannerData.HEADER)

    def set_banner_text(self):
        get_element_by_css_selector(self.driver, self.BANNER_TEXT).send_keys(BannerData.TEXT)

    def set_banner_link(self):
        get_element_by_xpath(self.driver, self.BANNER_LINK).send_keys(BannerData.LINK)

    def set_banner_img(self):
        FILE_PATH = BannerData.IMG
        get_element_by_css_selector(self.driver, self.BANNER_IMG).send_keys(FILE_PATH)
        get_element_by_css_selector(self.driver, self.IMG_CROPPER).click()

    @staticmethod
    def waiting(driver):
        banners = driver.find_elements_by_class_name("banner-preview__img")
        for banner in banners:
            if banner.value_of_css_property("display") == 'block':
                return banner

    def save_banner(self):
        banner = WebDriverWait(self.driver, 30, 0.1).until(self.waiting)
        WebDriverWait(banner, 30, 0.1).until(
            lambda d: (d.value_of_css_property("background-image") is not None)
        )
        get_element_by_css_selector(self.driver, self.SAVE_BUTTON).click()

    def get_banner_header(self):
        return get_element_by_xpath(self.driver, self.PREVIEW_BANNER_HEADER).text

    def get_banner_text(self):
        return get_element_by_xpath(self.driver, self.PREVIEW_BANNER_TEXT).text


class MainButton(Component):
    BUTTON = '.main-button-new'

    def click_to_main_button(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BUTTON)
        ).click()


class AgeRestrictions(Component):
    RESTRICT = '//*[@id="restrict-{}"]'.format(AgeRestrictionsData.AGE)
    RESTRICT_VIEW = '[data-node-id="restrict"]'
    RESTRICT_BANNER_VIEW = '//span[@class="banner-preview__title-wrapper"]//' \
                           'span[@class="banner-preview__age-limit js-age-title-restrictions"]'

    def show_age_restrictions(self):
        WebDriverWait(self.driver, 30, 1).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.RESTRICT_VIEW))
        ).click()

    def set_age_restrictions(self):
        get_element_by_xpath(self.driver, self.RESTRICT).click()

    def get_age_restrictions(self):
        return get_element_by_css_selector(self.driver, self.RESTRICT_VIEW).text

    def get_age_restrictions_from_banner_preview(self):
        return get_element_by_xpath(self.driver, self.RESTRICT_BANNER_VIEW).text


class Interests(Component):
    SHOW_INTERESTS = '[data-node-id="interests"]'
    SHOW_SELECTED_SUB_INTERESTS = '.campaign-setting__chosen-box__item__children'
    INTEREST = '[data-node-id="Авто"]'
    ALL_SUB_INTERESTS = '//*[@id="view2320"]'
    SUB_INTEREST = '//*[@id="interests{}"]/input'

    SUB_INTEREST_VIEW = '//ul[@class="campaign-setting__chosen-box__body"]//li[@data-id="{}"]'
    SUB_INTEREST_BUBBLE_VIEW = '//ul[@class="campaign-setting__chosen-box__bubble-list"]//li[@data-id="{}"]'
    DELETE_SUB_INTEREST = '//ul[@class="campaign-setting__chosen-box__body"]//li[@data-id="{}"]/span[2]'
    DELETE_SUB_INTEREST_BUBBLE = '//ul[@class="campaign-setting__chosen-box__bubble-list"]//li[@data-id="{}"]/span[2]'

    def show_interests(self):
        WebDriverWait(self.driver, 30, 2).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.SHOW_INTERESTS))
        ).click()

    def show_selected_sub_interests(self):
        WebDriverWait(self.driver, 30, 1).until(
            expected_conditions.staleness_of(
                get_element_by_css_selector(self.driver, self.SHOW_SELECTED_SUB_INTERESTS)
            )
        )
        get_element_by_css_selector(self.driver, self.SHOW_SELECTED_SUB_INTERESTS).click()

    def show_sub_interests(self):
        get_element_by_css_selector(self.driver, self.INTEREST).click()

    def select_all_sub_interests(self):
        get_element_by_css_selector(self.driver, self.ALL_SUB_INTERESTS).click()

    def select_sub_interest(self, interest_id):
        WebDriverWait(self.driver, 30, 1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.SUB_INTEREST.format(interest_id)))
        ).click()

    def get_selected_sub_interests(self, interest_id):
        return self.driver.find_element_by_xpath(self.SUB_INTEREST_VIEW.format(interest_id))

    def get_selected_sub_interests_from_bubble(self, interest_id):
        return self.driver.find_element_by_xpath(self.SUB_INTEREST_BUBBLE_VIEW.format(interest_id))

    def delete_sub_interest(self, interest_id):
        WebDriverWait(self.driver, 30, 1).until(
            expected_conditions.staleness_of(
                get_element_by_xpath(self.driver, self.DELETE_SUB_INTEREST.format(interest_id))
            )
        )
        get_element_by_xpath(self.driver, self.DELETE_SUB_INTEREST.format(interest_id)).click()

    def delete_sub_interest_from_bubble(self, interest_id):
        WebDriverWait(self.driver, 30, 1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.DELETE_SUB_INTEREST_BUBBLE.format(interest_id)))
        ).click()

    def get_value_of_deleted_sub_interest(self, interest_id):
        return get_element_by_xpath(self.driver, self.SUB_INTEREST.format(interest_id)).is_selected()




