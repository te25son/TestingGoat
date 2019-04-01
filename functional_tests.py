from selenium import webdriver
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
        self.fail("Finish the test!")

        # She is invited to enter a to-do item right from the get-go.

        # She types in "Buy himalayan salt". (Sandra heard about the amazing benifits of
        # himalayan salt from the same friend who told her about the app. She's sceptical
        # but scientific. She decides to try for herself.)

        # When she hits enter, the page updates. The page now lists "1: Buy himalayan salt"
        # as an item on her to-do list

        # There is still a text box inviting her to add another to-do item. She types
        # "Download the audiobooks - 'The Amazing Benefits of Himalayan Salt' and 'Himalayan
        # Salt: Yogi Secret or Capitalist Scam'".
        # Sandra is very thorough with her research and plans to give her friend a complete feedback.

        # The page updates and shows both items on her list

        # Sandra wonders whether the site will remember her list. Then she notices that the site has
        # generated a unique URL for her -- there is some explanatory text to that effect.

        # She visits that URL and... her to-do list is still there!

        # Satisfied, she begins to make herself a bath.


if __name__ == '__main__':
    unittest.main(warnings='ignore')
