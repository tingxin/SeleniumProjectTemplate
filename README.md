# Selenium Quick Start for Python API

Selenium automates browsers. That's it! What you do with that power is entirely up to you. Primarily, it is for automating web applications for testing purposes, but is certainly not limited to just that. Boring web-based administration tasks can (and should!) also be automated as well.

Selenium has the support of some of the largest browser vendors who have taken (or are taking) steps to make Selenium a native part of their browser. It is also the core technology in countless other browser automation tools, APIs and frameworks.

[You can get more information from here](http://selenium-python.readthedocs.io/)

## Prerequisite
* This sample base on Python3
* You need install the Chrome browser version 54.0.2840.98  or later
* Mac or Linux is better

## Quick start
### Config test machine
* [Download the remote WebDriver and Selenium server from here in your test machine](https://github.com/tingxin/SeleniumQuickStart/tree/master/resource)
* If your test machine is windows, you need put chromedriver.exe file and selenium-server-standalone-3.x.x.jar in a  empty folder
* If your test machine is linux or mac, you need put chromedriver fine and selenium-server-standalone-3.x.x.jar in a  empty folder
* Open your terminal window or cmd window, cd to that folder, use this command:
    
        java -jar selenium-server-standalone-2.x.x.jar
While running the Selenium server, you could see a message looking like this:
        
        15:43:07.541 INFO - RemoteWebDriver instances should connect to: http://127.0.0.1:4444/wd/hub
The above line says that you can use this URL for connecting to remote WebDriver. Here are some examples:
    
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    
    driver = webdriver.Remote(
       command_executor='http://127.0.0.1:4444/wd/hub',
       desired_capabilities=DesiredCapabilities.CHROME)

### Run it in local machine
* Download the code in your new machine(you can execute code and run test case in same machine, but it is not good)
* Open terminal window and cd to SeleniumQuickStart folder
* Install python binding for Selenium
    
        sudo python3 setup.py install

for windows user, you should
    
        C:\Python35\Scripts\pip.exe install selenium
        
* Run follow command:
    
        sudo python3 main.py

### Run it using docker
* Download the code in your new machine(you can execute code and run test case in same machine, but it is not good)
* CD to the SeleniumProjectTemplate folder and execute follow command in terminal window:
    
        docker build -t selenium:test .
        docker run [image id]
      
## Python API Docs
[You can get more information from here](http://selenium-python.readthedocs.io/)
    
