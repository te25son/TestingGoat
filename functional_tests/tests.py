from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


MAX_WAIT = 10




class NewVisitorTest(LiveServerTestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()


    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


    def test_can_start_a_list_for_one_user(self):
        # Sandra has heard about this wicked new online to-do app, and
        # she goes to check out it's homepage.
        self.browser.get(self.live_server_url)

        # She notices that the header and page title mention something about
        # to-do lists, so she must be in the right spot.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item right from the get-go.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item'
        )

        # She types in "Buy himalayan salt". (Sandra heard about the amazing benifits of
        # himalayan salt from the same friend who told her about the app. She's sceptical
        # but scientific. She decides to try for herself.)
        inputbox.send_keys('Buy himalayan salt')

        # When she hits enter, the page updates. The page now lists "1: Buy himalayan salt"
        # as an item on her to-do list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy himalayan salt')

        # There is still a text box inviting her to add another to-do item. She types
        # "Download the audiobooks - 'The Amazing Benefits of Himalayan Salt' and 'Himalayan
        # Salt: Yogi Secret or Capitalist Scam'".
        # Sandra is very thorough with her research and plans to give her friend a complete feedback.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Download the audiobooks - 'The Amazing Benefits of Himalayan Salt' and 'Himalayan Salt: Yogi Secret or Capitalist Scam'")
        inputbox.send_keys(Keys.ENTER)

        # The page updates and shows both items on her list
        self.wait_for_row_in_list_table('1: Buy himalayan salt')
        self.wait_for_row_in_list_table('2: Download the audiobooks - \'The Amazing Benefits of Himalayan Salt\' and \'Himalayan Salt: Yogi Secret or Capitalist Scam\'')

        # Satisfied, she begins to make herself a bath.


    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Sandra starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy himalayan salt')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy himalayan salt')

        # She notices that her list has a unique url
        sandra_list_url = self.browser.current_url
        self.assertRegex(sandra_list_url, '/lists/.+')

        # Now a new user, Georgio, comes along to the site

        ## We use a new browser session to assure that no information
        ## of Sandras is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Georgio visits the home page. There is no sign of Sandra's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy himalayan salt', page_text)
        self.assertNotIn('2: Download the audiobooks - \'The Amazing Benefits of Himalayan Salt\' and \'Himalayan Salt: Yogi Secret or Capitalist Scam\'', page_text)

        # Georgio starts a new list by entering a new item. He
        # is less interesting than Sandra
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Georgio also gets his own unique url
        georgio_list_url = self.browser.current_url
        self.assertRegex(georgio_list_url, '/lists/.+')
        self.assertNotEqual(georgio_list_url, sandra_list_url)

        # Again, there is no trace of Sandra's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy himalayan salt', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, Georgio takes a nap


    def test_layout_and_styling(self):
        # Sandra goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        # She starts a new list and sees the input is nicely centered
        # there too
        inputbox.send_keys('Testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Testing')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
