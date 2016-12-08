import os
import sys
import unittest
from common.config import config
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestCases(unittest.TestCase):

    def setUp(self):
        if "TEST_MACHINE" in os.environ:
            test_machine = os.environ["TEST_MACHINE"]
        elif "TEST_MACHINE" in config:
            test_machine = config["TEST_MACHINE"]
        elif len(sys.argv) > 1:
            test_machine = sys.argv[1]

        else:
            test_machine = ""
        print("remote server is " + test_machine)
        if len(test_machine) > 0:
            try:
                self.driver = webdriver.Remote(
                    command_executor=test_machine,
                    desired_capabilities=DesiredCapabilities.CHROME)
            except:
                self.fail(sys.exc_info()[1])
        else:
            self.fail("Can not init web driver")

    def tearDown(self):
        self.driver.close()