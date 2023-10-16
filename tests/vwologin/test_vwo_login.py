import logging
import time
import allure
import pytest
from selenium import webdriver

from src.pageObjectModel.loginPage import PageLogin


class TestVWOLogin:

    @pytest.fixture()
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://app.vwo.com")
        yield driver
        driver.quit()

    @allure.feature("VWO Login")
    @allure.title("APP VWO Login Test Case")
    @allure.id(1)
    @allure.story("App VWO Story")
    @allure.description("Verify that login is successful on app.com")
    @pytest.mark.positive
    def test_app_vwo_login_valid(self, driver):
        log = logging.getLogger(__name__)
        loginPage = PageLogin(driver)

        loginPage.vwo_login("contact+augg@thetestingacademy.com", "Wingify@123")
        time.sleep(5)
        assert "Dashboard" in driver.title
        time.sleep(2)
