# coding=utf-8
__author__ = 'alexander'

from selenium.webdriver.support.ui import Select, WebDriverWait
from constans import CSSSelectors, BannerData, AgeRestrictionsData


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
        self.driver.find_element_by_xpath(self.TARGET).click()

    def set_playground(self):
        self.driver.find_element_by_xpath(self.PLAYGROUND).click()

    def set_campaign_name(self):
        campaign_name = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.CAMPAIGN_NAME)
        )
        campaign_name.clear()
        campaign_name.send_keys(self.CAMPAIGN)


class Banner(Component):
    BANNER_HEADER = '[data-name="title"] .banner-form__input'
    BANNER_TEXT = '[data-name="text"] .banner-form__input_text-area'
    BANNER_LINK = './/li[@data-top="false"]//input[@data-name="url"]'
    BANNER_IMG = '.banner-form__img-file'
    IMG_CROPPER = '.image-cropper__save'
    SAVE_BUTTON = '.banner-form__save-button'

    PREVIEW_BANNER_HEADER = '.banner-preview__title'
    PREVIEW_BANNER_TEXT = '.banner-preview__text'

    def set_banner_header(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BANNER_HEADER)
        ).send_keys(BannerData.HEADER)

    def set_banner_text(self):
        self.driver.find_element_by_css_selector(self.BANNER_TEXT).send_keys(BannerData.TEXT)

    def set_banner_link(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.BANNER_LINK)
        ).send_keys(BannerData.LINK)

    def set_banner_img(self):
        FILE_PATH = BannerData.IMG
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BANNER_IMG)
        )
        element.send_keys(FILE_PATH)
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.IMG_CROPPER)
        ).click()

    def show_preview(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SAVE_BUTTON)
        ).click()

    def get_banner_header(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PREVIEW_BANNER_HEADER).text
        )

    def get_banner_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PREVIEW_BANNER_TEXT).text
        )


class MainButton(Component):
    BUTTON = '.main-button-new'

    def click_to_main_button(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BUTTON)
        ).click()


class AgeRestrictions(Component):
    RESTRICT = '//*[@id="restrict-{}"]'.format(AgeRestrictionsData.AGE)
    RESTRICT_VIEW = '[data-node-id="restrict"]'
    RESTRICT_BANNER_VIEW = '/html/body/div[1]/div[5]/' \
                           'div/div[2]/div/div[1]/div[3]/div/div[1]/div/div/div[1]/span/span[2]'

    def show_age_restrictions(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.RESTRICT_VIEW)
        ).click()

    def set_age_restrictions(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.RESTRICT)
        ).click()

    def get_age_restrictions(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.RESTRICT_VIEW).text
        )

    def get_age_restrictions_from_banner_preview(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.RESTRICT_BANNER_VIEW).text
        )


class Interests(Component):
    SHOW_INTERESTS = '[data-node-id="interests"]'
    SHOW_SELECTED_SUB_INTERESTS = '.campaign-setting__chosen-box__item__children'
    INTEREST = '[data-node-id="Авто"]'
    ALL_SUB_INTERESTS = '//*[@id="view2320"]'
    SUB_INTEREST = '//*[@id="interests{}"]/input'

    SUB_INTEREST_VIEW = '[data-id="{}"]'
    DELETE_SUB_INTEREST = '//*[@data-id="{}"]/span[2]'

    def show_interests(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SHOW_INTERESTS)
        ).click()

    def show_selected_sub_interests(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SHOW_SELECTED_SUB_INTERESTS)
        ).click()

    def show_sub_interests(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.INTEREST)
        ).click()

    def select_all_sub_interests(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ALL_SUB_INTERESTS)
        ).click()

    def select_sub_interest(self, interest_id):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUB_INTEREST.format(interest_id))
        ).click()

    def get_selected_sub_interests(self, interest_id):
        return self.driver.find_element_by_css_selector(self.SUB_INTEREST_VIEW.format(interest_id))

    def delete_sub_interest(self, interest_id):
        buf = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DELETE_SUB_INTEREST.format(interest_id))
        )
        buf.click()

    def get_value_of_deleted_sub_interest(self, interest_id):
        return self.driver.find_element_by_xpath(self.SUB_INTEREST.format(interest_id)).is_selected()




