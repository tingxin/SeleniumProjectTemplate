from common.testcases import TestCases
from selenium.webdriver.common.keys import Keys
import time

class WorkflowTestCases(TestCases):

    def test_search_many_times(self):
        print("Test searching in DevNet")

        driver = self.driver
        test_keys = ["deviot", "cmx", "aci", "sdn"]
        for i in range(0, len(test_keys)):
            driver.get("https://developer.cisco.com/site/devnet/home/index.gsp")
            self.assertIn("Cisco Devnet", driver.title)
            elem = driver.find_element_by_name("q")
            elem.send_keys(test_keys[i])
            elem.send_keys(Keys.RETURN)
            assert "Cisco DevNet: DevNetCreations - DevIoT" not in driver.page_source
            time.sleep(1)

