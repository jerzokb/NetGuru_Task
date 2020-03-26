import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):  # uruchamia się przed wszystkimi testami
        self.driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')

    def test_create_account(self):
        driver = self.driver
        url = 'http://automationpractice.com/index.php'
        driver.get(url)
        sign_in_button = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        sign_in_button.click()
        time.sleep(3)
        #Create account - Invalid email address Test
        create_account_email = driver.find_element_by_xpath('//*[@id="email_create"]')
        create_account_email.clear()
        create_account_email.send_keys('beata@test')
        create_account_button = driver.find_element_by_xpath('//*[@id="SubmitCreate"]/span')
        create_account_button.click()
        time.sleep(3)
        invalid_email_alert = driver.find_element_by_xpath('//*[@id="create_account_error"]/ol/li')
        print(f'Text displayed: {invalid_email_alert.text}')
        self.assertEqual('Invalid email address.', invalid_email_alert.text,
                         f'Expected alert "Invalid email address." differ from actual alert {invalid_email_alert.text}')
        # Create account - An account using this email address has already been registered Test
        create_account_email.clear()
        create_account_email.send_keys('aaa@aaa.com')
        create_account_button = driver.find_element_by_xpath('//*[@id="SubmitCreate"]/span')
        create_account_button.click()
        time.sleep(3)
        email_exist_alert = driver.find_element_by_xpath('//*[@id="create_account_error"]/ol/li')
        print(f'Text displayed: {email_exist_alert.text}')
        self.assertEqual('An account using this email address has already been registered. Please enter a valid password or request a new one.',
                         email_exist_alert.text,
                         f'Expected alert "An account using this email address has already been registered. Please enter a valid password or request a new one." '
                         f'differ from actual alert {email_exist_alert.text}')
        # Create account success Test
        create_account_email.clear()
        create_account_email.send_keys('beata@test1.net')
        create_account_button = driver.find_element_by_xpath('//*[@id="SubmitCreate"]/span')
        create_account_button.click()
        time.sleep(3)
        self.assertEqual('http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation',
                         driver.current_url,
                         f'Expected url differ from current url {driver.current_url}')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()