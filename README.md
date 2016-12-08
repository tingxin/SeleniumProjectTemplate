# Selenium Quick Start for Python API

Selenium automates browsers. That's it! What you do with that power is entirely up to you. Primarily, it is for automating web applications for testing purposes, but is certainly not limited to just that. Boring web-based administration tasks can (and should!) also be automated as well.

Selenium has the support of some of the largest browser vendors who have taken (or are taking) steps to make Selenium a native part of their browser. It is also the core technology in countless other browser automation tools, APIs and frameworks.

[You can get more information from here](http://selenium-python.readthedocs.io/)

## Prerequisite
* This sample base on Python3
* You need install the Chrome browser version 54.0.2840.98  or later
* Mac or Linux is better

## Quick start

* Download the code
* Open terminal window and cd to SeleniumQuickStart folder
* Install python binding for Selenium
    
        sudo python3 setup.py install

for windows user, you should
    
        C:\Python35\Scripts\pip.exe install selenium
        
* Run follow command:
    
        sudo python3 app.py
     
## Sample walk through
Initially, all the basic modules required are imported. The unittest module is a built-in Python based on Java’s JUnit. This module provides the framework for organizing the test cases. The selenium.webdriver module provides all the WebDriver implementations. Currently supported WebDriver implementations are Firefox, Chrome, Ie and Remote. The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.

    import unittest
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

The test case class is inherited from unittest.TestCase. Inheriting from TestCase class is the way to tell unittest module that this is a test case:

class DevNetTestCases(unittest.TestCase):
The setUp is part of initialization, this method will get called before every test function which you are going to write in this test case class. Here you are creating the instance of Chrome WebDriver.

    def setUp(self):
        import os
        import platform

        dir_path = os.path.dirname(os.path.realpath(__file__))
        if platform.system() == "Windows":
            chrome_driver_path = dir_path + "\\resource\\chromedriver"
        else:
            chrome_driver_path = dir_path + "/resource/chromedriver"
        self.driver = webdriver.Chrome(chrome_driver_path)
        
This is the test case method. The test case method should always start with characters test. The first line inside this method create a local reference to the driver object created in setUp method.

    def test_search_in_devnet(self):
            driver = self.driver
            
The driver.get method will navigate to a page given by the URL. WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired) before returning control to your test or script. It’s worth noting that if your page uses a lot of AJAX on load then WebDriver may not know when it has completely loaded.:

        driver.get("https://developer.cisco.com/site/devnet/home/index.gsp")

The next line is an assertion to confirm that title has “Cisco Devnet” word in it:

        self.assertIn("Cisco Devnet", driver.title)
        
WebDriver offers a number of ways to find elements using one of the find_element_by_* methods. For example, the input text element can be located by its name attribute using find_element_by_name method. Detailed explanation of finding elements is available in the Locating Elements chapter:

        elem = driver.find_element_by_name("q")

Next we are sending keys, this is similar to entering keys using your keyboard. Special keys can be send using Keys class imported from selenium.webdriver.common.keys:

    elem.send_keys("deviot")
    elem.send_keys(Keys.RETURN)
After submission of the page, you should get result as per search if there is any. To ensure that some results are found, make an assertion:

    assert "Cisco DevNet: DevNetCreations - DevIoT" not in driver.page_source

The tearDown method will get called after every test method. This is a place to do all cleanup actions. In the current method, the browser window is closed. You can also call quit method instead of close. The quit will exit the entire browser, whereas close will close a tab, but if it is the only tab opened, by default most browser will exit entirely.:

    def tearDown(self):
        self.driver.close()

Final lines are some boiler plate code to run the test suite:

    if __name__ == "__main__":
        unittest.main()
        
        
## Using Selenium with remote WebDriver
* To use the remote WebDriver, you should have Selenium server running. To run the server, use this command:
    
        java -jar selenium-server-standalone-2.x.x.jar
While running the Selenium server, you could see a message looking like this:
        
        15:43:07.541 INFO - RemoteWebDriver instances should connect to: http://127.0.0.1:4444/wd/hub
The above line says that you can use this URL for connecting to remote WebDriver. Here are some examples:
    
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    
    driver = webdriver.Remote(
       command_executor='http://127.0.0.1:4444/wd/hub',
       desired_capabilities=DesiredCapabilities.CHROME)
       
       
## Python API Docs
[You can get more information from here](http://selenium-python.readthedocs.io/)
    
