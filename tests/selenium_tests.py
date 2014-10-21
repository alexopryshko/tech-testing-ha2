# coding=utf-8
__author__ = 'alexander'

import os
import unittest
from selenium.webdriver import Remote, DesiredCapabilities
from objects.pages import CreatePage, AuthPage
from objects.constans import UserData, BannerData, AgeRestrictionsData


class SeleniumTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_domain(UserData.USER_DOMAIN)
        auth_form.set_login(UserData.USERNAME)
        auth_form.set_password(UserData.PASSWORD)
        auth_form.submit()

        self.create_page = CreatePage(self.driver)
        self.create_page.open()

    def tearDown(self):
        self.driver.quit()

    def test_authentication_user(self):
        email = self.create_page.top_menu.get_email()
        self.assertEqual(UserData.USERNAME + UserData.USER_DOMAIN, email)

    def test_banner_preview(self):
        base_settings = self.create_page.base_settings
        base_settings.set_target()
        base_settings.set_campaign_name()
        base_settings.set_playground()

        banner = self.create_page.banner
        banner.set_banner_header()
        banner.set_banner_link()
        banner.set_banner_text()
        banner.set_banner_img()
        banner.save_banner()

        self.assertEquals(BannerData.HEADER, banner.get_banner_header())
        self.assertEquals(BannerData.TEXT, banner.get_banner_text())

    def test_age_restrictions(self):
        age_restrictions = self.create_page.age_restrictions
        age_restrictions.show_age_restrictions()
        age_restrictions.set_age_restrictions()

        self.assertEquals(AgeRestrictionsData.AGE, age_restrictions.get_age_restrictions())
        self.assertEquals(AgeRestrictionsData.AGE, age_restrictions.get_age_restrictions_from_banner_preview())

    def test_select_several_sub_interests_less_six(self):
        interests = self.create_page.interests
        interests.show_interests()
        interests.show_sub_interests()
        for i in xrange(2, 7):
            interests.select_sub_interest(i)
        result = True
        try:
            for i in xrange(2, 7):
                interests.get_selected_sub_interests(i)
        except Exception:
            result = False
        self.assertTrue(result)

    def test_select_several_sub_interests_more_than_six(self):
        interests = self.create_page.interests
        interests.show_interests()
        interests.show_sub_interests()
        for i in xrange(2, 10):
            interests.select_sub_interest(i)
        interests.show_selected_sub_interests()
        result = True
        try:
            for i in xrange(2, 10):
                interests.get_selected_sub_interests_from_bubble(i)
        except Exception:
            result = False
        self.assertTrue(result)

    def test_delete_sub_interests_less_six(self):
        deleted_interest = 5
        interests = self.create_page.interests
        interests.show_interests()
        interests.show_sub_interests()
        for i in xrange(2, 7):
            interests.select_sub_interest(i)
        interests.delete_sub_interest(deleted_interest)
        self.assertFalse(interests.get_value_of_deleted_sub_interest(deleted_interest))

    def test_delete_sub_interests_more_than_six(self):
        interests = self.create_page.interests
        interests.show_interests()
        interests.show_sub_interests()
        for i in xrange(2, 10):
            interests.select_sub_interest(i)
        interests.show_selected_sub_interests()
        interests.delete_sub_interest_from_bubble(5)
        self.assertFalse(interests.get_value_of_deleted_sub_interest(5))







