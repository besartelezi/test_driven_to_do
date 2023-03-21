from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

# Tests are organized into classes, which inherit from unittest.TestCase
class NewVisitorTest(unittest.TestCase):  

    #* setUp and tearDown = SPECIAL METHODS that get run before and after each test
    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    #* any method whose name starts with test is a test method, and it will be run by the test runner
    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists

        #* assertin = special test assertions, look at documentation to check them all
        self.assertIn('To-Do', self.browser.title)  
        # #* self.fail = fails no matter what
        # Best to place this test at the end of all written tests, and remove it once all tests have been added
        # self.fail('Finish the test!')  
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        #* .send_keys = selenium's way of inputting keys
        inputbox.send_keys('Buy peacock feathers')  

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        #* Keys class lets us input special keys, like ENTER
        inputbox.send_keys(Keys.ENTER) 
        #* The time.sleep is there to make sure the browser has finished loading before we make any assertions about the new page
        time.sleep(1)


        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')  
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )
        
        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

#! checks if it's been executed from command line, rather than imported from another script
if __name__ == '__main__':  
    #* calling unittest main, launches unittest test runner which automatically finds test classes and methods in the file and runs them
    unittest.main()