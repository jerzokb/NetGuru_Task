import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):  #run before all tests
        self.driver = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe')

    def test_sign_on_account(self):
        driver = self.driver
        url = 'http://automationpractice.com/index.php'
        driver.get(url)
        sign_in_button = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        sign_in_button.click()
        time.sleep(3)
        #Sign In - Invalid emial Test
        sign_in_email = driver.find_element_by_xpath('//*[@id="email"]')
        sign_in_password = driver.find_element_by_xpath('//*[@id="passwd"]')
        submit_login_button = driver.find_element_by_xpath('//*[@id="SubmitLogin"]/span')
        sign_in_email.clear()
        sign_in_password.clear()
        sign_in_email.send_keys('beata@test')
        submit_login_button.click()
        time.sleep(3)
        invalid_email_alert = driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/ol/li')
        print(f'Text displayed: {invalid_email_alert.text}')
        self.assertEqual('Invalid email address.', invalid_email_alert.text,
                         f'Expected alert "Invalid email address." differ from actual alert {invalid_email_alert.text}')
        #Sign In - Password Required Test
        sign_in_email = driver.find_element_by_xpath('//*[@id="email"]')
        sign_in_password = driver.find_element_by_xpath('//*[@id="passwd"]')
        sign_in_email.clear()
        sign_in_password.clear()
        sign_in_email.send_keys('beata@test1.net')
        submit_login_button = driver.find_element_by_xpath('//*[@id="SubmitLogin"]/span')
        submit_login_button.click()
        time.sleep(3)
        password_required_alert = driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/ol/li')
        print(f'Text displayed: {password_required_alert.text}')
        self.assertEqual('Password is required.', password_required_alert.text,
                         f'Expected alert "Password is required." differ from actual alert {password_required_alert.text}')
        # Sign In - Athentication Failed Test
        sign_in_email = driver.find_element_by_xpath('//*[@id="email"]')
        sign_in_password = driver.find_element_by_xpath('//*[@id="passwd"]')
        submit_login_button = driver.find_element_by_xpath('//*[@id="SubmitLogin"]/span')
        sign_in_email.clear()
        sign_in_password.clear()
        sign_in_email.send_keys('beata@test1.net')
        sign_in_password.send_keys('tester123')
        submit_login_button.click()
        time.sleep(3)
        authentication_failed_alert = driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/ol/li')
        print(f'Text displayed: {authentication_failed_alert.text}')
        self.assertEqual('Authentication failed.', authentication_failed_alert.text,
                         f'Expected alert "Authentication failed." differ from actual alert {authentication_failed_alert.text}')
        #Sign in - Sign In correct test
        sign_in_email = driver.find_element_by_xpath('//*[@id="email"]')
        sign_in_password = driver.find_element_by_xpath('//*[@id="passwd"]')
        submit_login_button = driver.find_element_by_xpath('//*[@id="SubmitLogin"]/span')
        sign_in_email.clear()
        sign_in_password.clear()
        sign_in_email.send_keys('beata@test2.net')
        sign_in_password.send_keys('tester123')
        submit_login_button.click()
        time.sleep(3)
        print(f'Current url is: {driver.current_url}')
        self.assertEqual('http://automationpractice.com/index.php?controller=my-account',
                         driver.current_url,
                         f'Expected alert url differ from actual url {driver.current_url}')
        signed_on_user = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a/span')
        print(f'Signed in user: {signed_on_user.text}')
        self.assertEqual('Beata Tester',
                         signed_on_user.text,
                         f'Expected user "Beata Tester" differ from current user {signed_on_user.text}')


    @classmethod
    def tearDownClass(self):
        self.driver.quit()