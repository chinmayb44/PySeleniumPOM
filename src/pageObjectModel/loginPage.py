# Page Actions
# Page Attributes
from selenium.webdriver.common.by import By


class PageLogin:

    # WebDriver INit

    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    username = (By.ID, "login-username")
    password = (By.ID, "login-password")
    submit_button = (By.ID, "js-login-btn")

    error_msg = (By.CSS_SELECTOR, "#js-notification-box-msg")

    # forgot_password
    # start_a_free_trial

    # Return a WebElement -> username

    def get_username(self):
        return self.driver.find_element(*PageLogin.username)

    def get_password(self):
        return self.driver.find_element(*PageLogin.password)

    def get_submit_button(self):
        return self.driver.find_element(*PageLogin.submit_button)

    def get_error_message(self):
        return self.driver.find_element(*PageLogin.error_msg)

    # Page Actions

    def vwo_login(self,usrname,pwd):
        #get the username and send keys -email
        self.get_username().send_keys(usrname)

        #get the password and send keys -password

        self.get_password().send_keys(pwd)

        #click on the submit button and navigate to the dashboard
        self.get_submit_button().click()
