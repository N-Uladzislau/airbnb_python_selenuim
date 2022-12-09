from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException, \
    ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import helpers as H
import time
import unittest
import HtmlTestRunner
import AllureReports

class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_1_login_in(self):
        driver = self.driver

        # Open Browser
        driver.get(H.airbnb_url)
        print("______________________Positive_Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "Test 1 Verify that User able to 'Log In'\n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # Wait from 1s - 3s
        H.delay1_3()
        # check API use -> POM
        H.check_API(driver)
        # check that
        H.asser_title(driver, "Vacation Homes & Condo Rentals - Airbnb - Airbnb")
        # close "ad"
        driver.find_element(By.XPATH, '//button[@class="czcfm7x dir dir-ltr"]').click()
        time.sleep(1)
        # verify that main LOGO is present
        H.main_logo(driver)
        time.sleep(1)
        # Log in into account
        H.log_in(driver)
        time.sleep(2)
        print("Test Passed user able to Log in into account")

    def test_2_search_for_a_place(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        # Open Browser
        driver.get(H.airbnb_url)
        time.sleep(1)
        print("______________________Positive_Test___________________________")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              "Test 2 Search for a place \n"
              "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # Wait from 1s - 3s
        H.delay1_3()
        # check API use -> POM
        H.check_API(driver)
        # check that
        H.asser_title(driver, "Vacation Homes & Condo Rentals - Airbnb - Airbnb")
        # close "ad"
        driver.find_element(By.XPATH, '//button[@class="czcfm7x dir dir-ltr"]').click()
        time.sleep(1)
        H.log_in(driver)
        # El "Anywhere" is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Anywhere"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Anywhere"]')))
        # click on Button "Anywhere"
        driver.find_element(By.XPATH, '//*[text()="Anywhere"]').click()
        time.sleep(3)
        # Placeholder "Search Destinations" is visible and clickable
        wait.until(EC.visibility_of_element_located((By.ID, 'bigsearch-query-location-input')))
        wait.until(EC.element_to_be_clickable((By.ID, 'bigsearch-query-location-input')))
        # Enter value "Barcelona, Spain"
        driver.find_element(By.ID, 'bigsearch-query-location-input').send_keys("Barcelona, Spain")
        driver.find_element(By.ID, "bigsearch-query-location-input").send_keys(Keys.ENTER)
        time.sleep(1)
        # button "I'm flexible" is visible and clickable
        wait.until(EC.visibility_of_element_located((By.ID, 'tab--tabs--1')))
        wait.until(EC.element_to_be_clickable((By.ID, 'tab--tabs--1')))
        # Click on button "I'm flexible"
        driver.find_element(By.ID, 'tab--tabs--1').click()
        time.sleep(1)
        # choose stay for "Weekend"
        # button "Weekend" is visible and clickable
        wait.until(EC.visibility_of_element_located((By.ID, "flexible_trip_lengths-weekend_trip")))
        wait.until(EC.element_to_be_clickable((By.ID, "flexible_trip_lengths-weekend_trip")))
        # Click on button "Weekend"
        driver.find_element(By.ID, "flexible_trip_lengths-weekend_trip").click()
        # click on arrow "next"
        driver.find_element(By.XPATH, '//button[@aria-label="Next"][@class="_1elq749"]').click()
        time.sleep(1)
        # month "July" is visible and clickable
        wait.until(EC.visibility_of_element_located((By.ID, "flexible_trip_dates-july")))
        wait.until(EC.element_to_be_clickable((By.ID, "flexible_trip_dates-july")))
        # # choose month "July"
        driver.find_element(By.ID, "flexible_trip_dates-july").click()
        time.sleep(3)
        # Add Guests
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[text()="Who"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Who"]')))
        # # choose month "July"
        driver.find_element(By.XPATH, '//div[text()="Who"]').click()
        time.sleep(1)
        # add two "Adults" use POM
        H.add_two_adults(driver)
        time.sleep(1)
        # add two "Children" use POM
        H.add_two_children(driver)
        time.sleep(1)
        # Pets button is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@data-testid="stepper-pets-increase-button"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="stepper-pets-increase-button"]')))
        # add One Pets
        driver.find_element(By.XPATH, '//*[@data-testid="stepper-pets-increase-button"]').click()
        # "Search"" button is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="_jxxpcd"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="_jxxpcd"]')))
        # click on "Search" button
        driver.find_element(By.XPATH, '//*[@class="_jxxpcd"]').click()
        time.sleep(1)
        H.change_currency(driver)
        time.sleep(2)
        # Open Filters
        driver.find_element(By.XPATH, '//*[@class="c1tureqs dir dir-ltr"]').click()
        time.sleep(2)
        # Change Price Range less than 400 -> POM
        H.price_less_400(driver)
        time.sleep(2)
        # choose "Entire Place"
        driver.find_element(By.NAME, "Entire place").click()
        time.sleep(2)
        # "show homes" is visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@aria-live="polite"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@aria-live="polite"]')))
        # click on button "Show homes"
        driver.find_element(By.XPATH, '//a[@aria-live="polite"]').click()
        time.sleep(3)
        # pick a 1st place
        # Place is visible and clickable
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                          '//img[@src="https://a0.muscache.com/im/pictures/9308e8fd-0d33-47b4-b5bd-fd9b55591dc5.jpg?im_w=720"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   '//img[@src="https://a0.muscache.com/im/pictures/9308e8fd-0d33-47b4-b5bd-fd9b55591dc5.jpg?im_w=720"]')))
            driver.find_element(By.XPATH,
                                '//img[@src="https://a0.muscache.com/im/pictures/9308e8fd-0d33-47b4-b5bd-fd9b55591dc5.jpg?im_w=720"]').click()
            # switch_to_another tab
            driver.switch_to.window(driver.window_handles[1])
            # Show all photo
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Listing image 1, Show all photos"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Listing image 1, Show all photos"]')))
            driver.find_element(By.XPATH, '//*[@aria-label="Listing image 1, Show all photos"]').click()
            time.sleep(2)
            # Open the first Photo
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='227861502']")))
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='227861502']")))
            driver.find_element(By.XPATH, "//*[@id='227861502']").click()
            time.sleep(1)
            # get screenshot of 1st house
            driver.get_screenshot_as_file("1st House Photo.png")

            # Click on the right arrow and go to the next page
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Next"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Next"]')))
            driver.find_element(By.XPATH, '//*[@aria-label="Next"]').click()
            time.sleep(1)
            # get screenshot 2nd photo
            driver.get_screenshot_as_file("1st House 2nd Photo.png")

            # Click on the right arrow and go to the next page
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Next"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Next"]')))
            driver.find_element(By.XPATH, '//*[@aria-label="Next"]').click()
            time.sleep(1)
            # close window with photos
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="_1f4biqmy"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="_1f4biqmy"]')))
            driver.find_element(By.XPATH, '//*[@class="_1f4biqmy"]').click()
            time.sleep(1)
            # close again
            driver.back()
            time.sleep(1)
            # scroll to Cancellation
            cancellation_p = '//*[text()="Cancellation policy"]'
            actions = ActionChains(driver)
            actions.move_to_element(driver.find_element(By.XPATH, cancellation_p)).perform()
            time.sleep(2)
            # Check that policy is present on the page
            self.assertIn('Cancellation policy', driver.page_source)
            time.sleep(1)
            wishlist = '//*[text()="Save"]'
            # move to wishlist
            actions.move_to_element(driver.find_element(By.XPATH, wishlist)).perform()
            # click on button "Wishlist"
            driver.find_element(By.XPATH, wishlist).click()
            time.sleep(3)
            # click on placeholder and enter Name of house
            driver.find_element(By.ID, 'name-list-input-save-to-list-modal').send_keys("1st Place")
            # "Create" button is visible and clickable
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Create']")))
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Create']")))
            driver.find_element(By.XPATH, "//*[text()='Create']").click()
            time.sleep(3)
            print("1st Place was added to wishlist")
        except NoSuchElementException:
            print("This house is already booked")
        driver.find_element(By.XPATH, '//*[text()="Start your search"]').click()
        time.sleep(3)
        # use pre-condition for choose place
        driver.find_element(By.XPATH, '//*[text()="Barcelona · Stays"]').click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                          '//img[@src="https://a0.muscache.com/im/pictures/8a03a725-c03f-4327-96b0-e18dfb507dcc.jpg?im_w=720"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   '//img[@src="https://a0.muscache.com/im/pictures/8a03a725-c03f-4327-96b0-e18dfb507dcc.jpg?im_w=720"]')))
            driver.find_element(By.XPATH,
                                '//img[@src="https://a0.muscache.com/im/pictures/8a03a725-c03f-4327-96b0-e18dfb507dcc.jpg?im_w=720"]').click()
            # switch_to_another tab
            driver.switch_to.window(driver.window_handles[2])
            # Show all photo
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Listing image 1, Show all photos"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Listing image 1, Show all photos"]')))
            driver.find_element(By.XPATH, '//*[@aria-label="Listing image 1, Show all photos"]').click()
            time.sleep(2)
            # Open the first Photo
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='483264433']")))
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='483264433']")))
            driver.find_element(By.XPATH, "//*[@id='483264433']").click()
            time.sleep(1)
            # get screenshot of 1st house
            driver.get_screenshot_as_file("2nd House Photo.png")

            # Click on the right arrow and go to the next page
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Next"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Next"]')))
            driver.find_element(By.XPATH, '//*[@aria-label="Next"]').click()
            time.sleep(1)
            # get screenshot 2nd photo
            driver.get_screenshot_as_file("2nd House 2nd Photo.png")

            # Click on the right arrow and go to the next page
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Next"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Next"]')))
            driver.find_element(By.XPATH, '//*[@aria-label="Next"]').click()
            time.sleep(1)
            # close window with photos
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="_1f4biqmy"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="_1f4biqmy"]')))
            driver.find_element(By.XPATH, '//*[@class="_1f4biqmy"]').click()
            time.sleep(1)
            # close again
            driver.back()
            time.sleep(1)
            # scroll to Cancellation
            cancellation_p = '//*[text()="Cancellation policy"]'
            actions = ActionChains(driver)
            actions.move_to_element(driver.find_element(By.XPATH, cancellation_p)).perform()
            time.sleep(2)
            # Check that policy is present on the page
            self.assertIn('Cancellation policy', driver.page_source)
            time.sleep(1)
            wishlist = '//*[text()="Save"]'
            # move to wishlist
            actions.move_to_element(driver.find_element(By.XPATH, wishlist)).perform()
            # click on button "Wishlist"
            driver.find_element(By.XPATH, wishlist).click()
            time.sleep(3)
            # click on "Create new wishlist"
            driver.find_element(By.XPATH, '//*[text()="Create new wishlist"]').click()
            time.sleep(1)
            # Enter Name of 2nd place
            driver.find_element(By.ID, "name-list-input-save-to-list-modal").send_keys("2nd Place")
            time.sleep(1)
            # "Create" button is visible and clickable
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Create']")))
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Create']")))
            driver.find_element(By.XPATH, "//*[text()='Create']").click()
            time.sleep(3)
            print("2nd Place was added to wishlist")
        except NoSuchElementException:
            print("This house is already booked")
        driver.find_element(By.XPATH, '//*[text()="Start your search"]').click()
        time.sleep(3)
        # use pre-condition for choose place
        driver.find_element(By.XPATH, '//*[text()="Barcelona · Stays"]').click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         '//img[@src="https://a0.muscache.com/im/pictures/4a36b860-4dff-421c-bbdc-503a0214f966.jpg?im_w=720"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH,
                                                   '//img[@src="https://a0.muscache.com/im/pictures/4a36b860-4dff-421c-bbdc-503a0214f966.jpg?im_w=720"]')))
            driver.find_element(By.XPATH,
                                '//img[@src="https://a0.muscache.com/im/pictures/4a36b860-4dff-421c-bbdc-503a0214f966.jpg?im_w=720"]').click()
            # switch_to_another tab
            driver.switch_to.window(driver.window_handles[3])
            # Show all photo
            wait.until(
                EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Listing image 1, Show all photos"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Listing image 1, Show all photos"]')))
            driver.find_element(By.XPATH, '//*[@aria-label="Listing image 1, Show all photos"]').click()
            time.sleep(2)
            # Open the first Photo
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='160787709']")))
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='160787709']")))
            driver.find_element(By.XPATH, "//*[@id='160787709']").click()
            time.sleep(1)
            # get screenshot of 1st house
            driver.get_screenshot_as_file("3rd House Photo.png")

            # Click on the right arrow and go to the next page
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Next"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Next"]')))
            driver.find_element(By.XPATH, '//*[@aria-label="Next"]').click()
            time.sleep(1)
            # get screenshot 2nd photo
            driver.get_screenshot_as_file("3rd House 2nd Photo.png")

            # Click on the right arrow and go to the next page
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Next"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Next"]')))
            driver.find_element(By.XPATH, '//*[@aria-label="Next"]').click()
            time.sleep(1)
            # close window with photos
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="_1f4biqmy"]')))
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="_1f4biqmy"]')))
            driver.find_element(By.XPATH, '//*[@class="_1f4biqmy"]').click()
            time.sleep(1)
            # close again
            driver.back()
            time.sleep(1)
            # scroll to Cancellation
            cancellation_p = '//*[text()="Cancellation policy"]'
            actions = ActionChains(driver)
            actions.move_to_element(driver.find_element(By.XPATH, cancellation_p)).perform()
            time.sleep(2)
            # Check that policy is present on the page
            self.assertIn('Cancellation policy', driver.page_source)
            time.sleep(1)
            wishlist = '//*[text()="Save"]'
            # move to wishlist
            actions.move_to_element(driver.find_element(By.XPATH, wishlist)).perform()
            # click on button "Wishlist"
            driver.find_element(By.XPATH, wishlist).click()
            time.sleep(3)
            # click on "Create new wishlist"
            driver.find_element(By.XPATH, '//*[text()="Create new wishlist"]').click()
            time.sleep(1)
            # Enter Name of 2nd place
            driver.find_element(By.ID, "name-list-input-save-to-list-modal").send_keys("3rd Place")
            time.sleep(1)
            # "Create" button is visible and clickable
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Create']")))
            wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Create']")))
            driver.find_element(By.XPATH, "//*[text()='Create']").click()
            time.sleep(3)
            print("3rd Place was added to wishlist")
        except NoSuchElementException:
            print("This house is already booked")
        # check wishlists
        wait.until(EC.visibility_of_element_located((By.XPATH, H.btnk_Log_in)))
        wait.until(EC.element_to_be_clickable((By.XPATH, H.btnk_Log_in)))
        driver.find_element(By.XPATH, H.btnk_Log_in).click()
        time.sleep(2)
        # Go to Wishlists
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="Wishlists"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Wishlists"]')))
        driver.find_element(By.XPATH, '//*[text()="Wishlists"]').click()
        time.sleep(2)
        # assert Title
        H.asser_title(driver, "Your lists · Wishlists - Airbnb")
        time.sleep(1)
        # Check 1st Place
        print(driver.find_element(By.XPATH, '//*[@id="FMP-target"]').get_attribute('src'))
        # Check 2nd Place
        print(driver.find_element(By.XPATH, '//img[@data-original-uri='
                                            '"https://a0.muscache.com/im/pictures/8a03a725-c03f-4327-96b0-e18dfb507dcc.jpg?im_w=720"]').get_attribute('src'))
        # Check 3rd Place
        print(driver.find_element(By.XPATH, '//img[@data-original-uri='
                                            '"https://a0.muscache.com/im/pictures/9308e8fd-0d33-47b4-b5bd-fd9b55591dc5.jpg?im_w=720"]').get_attribute('src'))

        # optional deleting places
        # if you wanna execute without, will be Error
        try:# Delete 1st Place
            driver.find_element(By.XPATH, '//*[@id="FMP-target"]').click()
            time.sleep(1)# //*[@data-testid="list-details-marquee__button-to-open-settings"]
            driver.find_element(By.XPATH, '//*[@data-testid="list-details-marquee__button-to-open-settings"]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//*[text()='Delete']").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//*[text()='Yes, delete']").click()
            time.sleep(1)

            # Delete 2nd Place
            driver.find_element(By.XPATH, '//img[@data-original-uri='
                                                '"https://a0.muscache.com/im/pictures/8a03a725-c03f-4327-96b0-e18dfb507dcc.jpg?im_w=720"]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@data-testid="list-details-marquee__button-to-open-settings"]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//*[text()='Delete']").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//*[text()='Yes, delete']").click()
            time.sleep(1)

            # Delete 3rd Place
            driver.find_element(By.XPATH, '//img[@data-original-uri='
                                                '"https://a0.muscache.com/im/pictures/9308e8fd-0d33-47b4-b5bd-fd9b55591dc5.jpg?im_w=720"]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@data-testid="list-details-marquee__button-to-open-settings"]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//*[text()='Delete']").click()
            time.sleep(1)
            driver.find_element(By.XPATH, "//*[text()='Yes, delete']").click()
            time.sleep(1)
            print("All places have been DELETED")
        except NoSuchElementException:
            print("All places have not been DELETED")


        # Log out from Account
        wait.until(EC.visibility_of_element_located((By.XPATH, H.btnk_Log_in)))
        wait.until(EC.element_to_be_clickable((By.XPATH, H.btnk_Log_in)))
        driver.find_element(By.XPATH, H.btnk_Log_in).click()
        time.sleep(1)
        # Click on button "Log out"
        driver.find_element(By.XPATH, '//*[text()="Log out"]').click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

if __name__ == "__main__":
    unittest.main(AllureReports)
