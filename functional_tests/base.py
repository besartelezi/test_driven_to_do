import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10


def wait(fn):
    # Using *args and **kwargs, we specify that modified_fn may take any arbitrary positional and keyword arguments
    def modified_fn(*args, **kwargs):  
        start_time = time.time()
        while True:  
            try:
                # As we’ve captured them in the function definition, we make sure to pass those same arguments to fn when we actually call it.
                return fn(*args, **kwargs)  
            except (AssertionError, WebDriverException) as e:  
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    return modified_fn  

# Tests are organized into classes, which inherit from unittest.TestCase
class FunctionalTest(StaticLiveServerTestCase):  

    #* setUp and tearDown = SPECIAL METHODS that get run before and after each test
    def setUp(self):  
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):  
        self.browser.quit()

    @wait
    def wait_for(self, fn):
        return fn()

    #* made a method that gets called in the test
    @wait
    def wait_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')


    @wait
    def wait_to_be_logged_in(self, email):
        self.browser.find_element_by_link_text('Log out')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(email, navbar.text)


    @wait
    def wait_to_be_logged_out(self, email):
        self.browser.find_element_by_name('email')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertNotIn(email, navbar.text)