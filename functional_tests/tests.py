from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




class NewVisitorTest(LiveServerTestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
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
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy himalayan salt')

        # There is still a text box inviting her to add another to-do item. She types
        # "Download the audiobooks - 'The Amazing Benefits of Himalayan Salt' and 'Himalayan
        # Salt: Yogi Secret or Capitalist Scam'".
        # Sandra is very thorough with her research and plans to give her friend a complete feedback.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Download the audiobooks - 'The Amazing Benefits of Himalayan Salt' and 'Himalayan Salt: Yogi Secret or Capitalist Scam'")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates and shows both items on her list
        self.check_for_row_in_list_table('1: Buy himalayan salt')
        self.check_for_row_in_list_table('2: Download the audiobooks - \'The Amazing Benefits of Himalayan Salt\' and \'Himalayan Salt: Yogi Secret or Capitalist Scam\'')

        # Sandra wonders whether the site will remember her list. Then she notices that the site has
        # generated a unique URL for her -- there is some explanatory text to that effect.

        # She visits that URL and... her to-do list is still there!

        # Satisfied, she begins to make herself a bath.
        self.fail("Finish the test!")
