# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


class TestHomePage(TestCase):
    
    def setUp(self):
        self.response = self.client.get(reverse("home"))
    
    def test_uses_index_template(self):        
        self.assertTemplateUsed(self.response, "feeder/index.html")
    
    def test_uses_base_template(self):
        self.assertTemplateUsed(self.response, "base.html")
