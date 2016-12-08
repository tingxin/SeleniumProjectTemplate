from common.testcases import TestCases
from selenium.webdriver.common.keys import Keys


class HomepageTestCases(TestCases):

    def test_search_in_devnet(self):
        print("Test searching in DevNet")

        driver = self.driver
        driver.get("https://developer.cisco.com/site/devnet/home/index.gsp")
        self.assertIn("Cisco Devnet", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("deviot")
        elem.send_keys(Keys.RETURN)
        assert "Cisco DevNet: DevNetCreations - DevIoT" not in driver.page_source

    def test_login_failed_in_devnet(self):
        print("Test login in use a un-auth user in DevNet")
        driver = self.driver
        driver.get("https://developer.cisco.com/site/devnet/home/index.gsp")
        self.assertIn("Cisco Devnet", driver.title)
        elem = driver.find_element_by_link_text("Log in")
        elem.click()
        self.assertIn("Cisco.com Login Page", driver.title)
        input_name = "testuser"
        password = "123456789"

        cec_name = driver.find_element_by_id("userInput")
        cec_name.send_keys(input_name)
        cec_pass = driver.find_element_by_id("passwordInput")
        cec_pass.send_keys(password)
        login_button = driver.find_element_by_id("login-button")
        login_button.click()
        self.assertIn("Login Page", driver.title)


