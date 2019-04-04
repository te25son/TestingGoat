from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest




class NewVisitorTest(unittest.TestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Sandra has heard about this wicked new online to-do app, and
        # she goes to check out it's homepage.
        self.browser.get('http://localhost:8000')

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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text == '1: Buy himalayan salt' for row in rows),
        #     f'New to-do item did not appear in the table. Contents were\n{table.text}'
        # )
        self.assertIn('1: Buy himalayan salt', [row.text for row in rows])

        # There is still a text box inviting her to add another to-do item. She types
        # "Download the audiobooks - 'The Amazing Benefits of Himalayan Salt' and 'Himalayan
        # Salt: Yogi Secret or Capitalist Scam'".
        # Sandra is very thorough with her research and plans to give her friend a complete feedback.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Download the audiobooks - 'The Amazing Benefits of Himalayan Salt' and 'Himalayan Salt: Yogi Secret or Capitalist Scam'")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates and shows both items on her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy himalayan salt', [row.text for row in rows])
        self.assertIn('2: Download the audiobooks - \'The Amazing Benefits of Himalayan Salt\' and \'Himalayan Salt: Yogi Secret or Capitalist Scam\'', [row.text for row in rows])

        # Sandra wonders whether the site will remember her list. Then she notices that the site has
        # generated a unique URL for her -- there is some explanatory text to that effect.

        # She visits that URL and... her to-do list is still there!

        # Satisfied, she begins to make herself a bath.
        self.fail("Finish the test!")


if __name__ == '__main__':
    unittest.main(warnings='ignore')
