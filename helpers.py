import time
import random
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
F = Faker()
import driver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver import ActionChains
actions = ActionChains(driver)
from selenium.webdriver.common.action_chains import ActionChains





# Url
airbnb_url = "https://www.airbnb.com/"
# Main Logo
main_logo = '//*[@class="l10sdlqs dir dir-ltr"]'
# btnk Log in
btnk_Log_in = '//*[@class="c1grjlav crawnjq dir dir-ltr"]'
# btnk increase adults
adult_increase_btnk = '//*[@data-testid="stepper-adults-increase-button"]'
# btnk increase Children 
children_increase_btnk = '//*[@data-testid="stepper-children-increase-button"]'









# Assert driver title
def asser_title(driver, title):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_is(title))
    assert title in driver.title
    print(f'Page has {driver.title} as Page title')
    # screenshot of page of title has different title
    driver.get_screenshot_as_file(f'Page has different {title}.png')
    if not title in driver.title:
        raise Exception(f'Page {title} has wrong title')


# Check API
def check_API(driver):
    code = requests.get(driver.current_url).status_code
    if code == 200:
        print(f"URL has : {requests.get(driver.current_url).status_code} as status")
    else:
        print("API has response code is not 200")

# Check that "MAIN LOGO" is present
def main_logo(driver):
    try:
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="l10sdlqs dir dir-ltr"]')))
        print("Logo is present and correct")
    except NoSuchElementException:
        print("Logo is NOT present on the Main Page")
        driver.get_screenshot_as_file("Page_Has_Different_Logo.png")

# add two adults
def add_two_adults(driver):
    wait = WebDriverWait(driver,10)
    # el increase is visible and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH, adult_increase_btnk)))
    wait.until(EC.element_to_be_clickable((By.XPATH, adult_increase_btnk)))
    # add first adult
    driver.find_element(By.XPATH, adult_increase_btnk).click()
    # add second adult
    driver.find_element(By.XPATH, adult_increase_btnk).click()

# add to Children
def add_two_children(driver):
    wait = WebDriverWait(driver,10)
    # el increase is visible and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH, children_increase_btnk)))
    wait.until(EC.element_to_be_clickable((By.XPATH, children_increase_btnk)))
    # add first adult
    driver.find_element(By.XPATH, children_increase_btnk).click()
    # add second adult
    driver.find_element(By.XPATH, children_increase_btnk).click()





# Log In into account
def log_in(driver):
    wait = WebDriverWait(driver, 10)
    try:  # Button visible and clickable
        wait.until(EC.visibility_of_element_located((By.XPATH, btnk_Log_in)))
        wait.until(EC.element_to_be_clickable((By.XPATH, btnk_Log_in)))
        # click on button
        driver.find_element(By.XPATH, btnk_Log_in).click()
        print("Log In Button is OK")
    except TimeoutException:
        print("Log In button is NOT OK")
    time.sleep(1)
    try: # inner button Log In
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in")))
        # Click on button Log In
        driver.find_element(By.LINK_TEXT, "Log in"). click()
        print("Inner button Log in is OK")
    except NoSuchElementException:
        print("Inner button Log in is NOT OK")
    # verify "continue with email"
    time.sleep(4)
    # "Continue with email" is present and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Continue with email')]")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Continue with email')]")))
    # Click on button "continue with email"
    driver.find_element(By.XPATH, "//div[contains(text(),'Continue with email')]").click()

    # placeholder Email is visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, "email-login-email")))
    wait.until(EC.element_to_be_clickable((By.ID, "email-login-email")))
    # Enter Email
    driver.find_element(By.ID, "email-login-email").send_keys("qwerty11111@gmail.com")

    # Button "Continue" is visible and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@data-testid="signup-login-submit-btn"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="signup-login-submit-btn"]')))
    # click on Button "Continue"
    driver.find_element(By.XPATH, '//*[@data-testid="signup-login-submit-btn"]').click()
    time.sleep(2)

    # placeholder Password is visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, "email-signup-password")))
    wait.until(EC.element_to_be_clickable((By.ID, "email-signup-password")))
    # Enter Password
    driver.find_element(By.ID, "email-signup-password").send_keys("Qwertyqwerty12345")

    # Button "Log in" is visible and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@data-testid="signup-login-submit-btn"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="signup-login-submit-btn"]')))
    driver.find_element(By.XPATH, '//*[@data-testid="signup-login-submit-btn"]').click()
    time.sleep(2)

''' max_price = driver.find_element(By.XPATH, '//input[@id="price_filter_max"]')
    max_price.clear()
    max_price.click()
    max_price.send_keys('100')'''
# Change currency from $ -> EUR
def change_currency(driver):
    wait = WebDriverWait(driver, 10)
    # el Currency and Language is visible and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Choose a language and currency"]')))
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Choose a language and currency"]')))
    # Click on button
    driver.find_element(By.XPATH, '//*[@aria-label="Choose a language and currency"]').click()
    # "Currency" button" is visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, 'tab--language_region_and_currency--1')))
    wait.until(EC.visibility_of_element_located((By.ID, 'tab--language_region_and_currency--1')))
    # Click on "Currency" button"
    driver.find_element(By.ID, 'tab--language_region_and_currency--1').click()

    # Currency EUR is visible and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="EUR – €"]')))
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="EUR – €"]')))
    # Click on "Currency EUR" button
    driver.find_element(By.XPATH, '//*[text()="EUR – €"]').click()

# Change Price less than 400
def price_less_401(driver):
    wait = WebDriverWait(driver, 10)
    # placeholder for "max price" visible and clickable
    #wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="price_filter_max"]')))
    #wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="price_filter_max"]')))
    actions = ActionChains(driver)
    max_price = driver.find_element(By.XPATH, '//input[@id="price_filter_max"]')
    actions.double_click(max_price).double_click(max_price).perform()
    driver.find_element(By.XPATH, '//input[@id="price_filter_max"]').send_keys(Keys.CLEAR)
    actions.send_keys("400").perform()

def price_less_400(driver):
    wait = WebDriverWait(driver, 10)
    max_price = driver.find_element(By.XPATH, '//input[@id="price_filter_max"]')
    # placeholder for "max price" visible and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="price_filter_max"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="price_filter_max"]')))
    # Use library actions for clear field "max Price"
    # double_click on field
    actions = ActionChains(driver)
    actions.double_click(max_price).double_click(max_price).perform()
    # clear field
    driver.find_element(By.XPATH, '//input[@id="price_filter_max"]').send_keys(Keys.CLEAR)
    # enter value 400
    actions.send_keys("400").perform()

















# driver sleep form 1s to 5s
def delay1_5():
    time.sleep(random.randint(1, 5))
# 1-3
def delay1_3():
    time.sleep(random.randint(1, 5))

