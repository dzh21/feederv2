# -*- coding:utf-8 -*-
from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class HomeNewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):        
        profile_name = '/home/dzh/.mozilla/firefox/elo3wssm.default'
        profile = webdriver.FirefoxProfile(profile_name)
        self.browser = webdriver.Firefox(firefox_profile=profile)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
        
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)
        
    def test_home_title(self):
        """ test base template loading """
        self.browser.get(self.get_full_url("home"))
        self.assertEqual("RSS reader", self.browser.title)          

    def test_h1_css(self):
        """ test static file loading """
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEquals(h1.value_of_css_property("color"),
            "rgba(200, 50, 255, 1)")

	def test_home_files(self):
		self.browser.get(self.live_server_url + "/robots.txt")
		self.assertNotIn("Not found", self.browser.title)
		self.browser.get(self.live_server_url + "/humans.txt")
		self.assertNotIn("Not found", self.browser.title)
