import time

import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenario:

    @pytest.mark.invaliduser
    @pytest.mark.parametrize("username, password, expected_error_message", [("student2", "Password123", "Your username is invalid!")])
    def test_negative_username(self, driver, username, password, expected_error_message):
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        # Type password Password123 into Password field

        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        time.sleep(5)
        # Pouch Submit button

        submitbutton_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submitbutton_locator.click()

        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message not displayed but it should"

        err_message = error_message_locator.text
        assert err_message == expected_error_message, "error message should be 'Your user name is invalid!'"
