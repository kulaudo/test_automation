import dependency_injector.providers as providers
import dependency_injector.containers as containers
from selenium import webdriver
from enum import Enum, auto
from selenium.webdriver.chrome.options import Options
import configparser
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#configparser.ConfigParser().read('')

class DriverFactory:
    
    def chrome_driver(self):
        return webdriver.Chrome(executable_path='E:\\chromedriver.exe')

    def firefox_driver(self):
        return webdriver.Firefox(executable_path='E:\\geckodriver.exe')

    def chromeheadless_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        return webdriver.Chrome(executable_path='E:\\chromedriver.exe', options=chrome_options)

    def remote_chrome_driver(self):
        return webdriver.Remote(
            command_executor='http://192.168.50.173:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

    def remote_firfox_driver(self):
        return webdriver.Remote(
            command_executor='http://192.168.50.173:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX)

    def remote_ie_driver(self):
        return webdriver.Remote(
            command_executor='http://192.168.50.173:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
            
                

class DriverService(containers.DeclarativeContainer):
    
    Chrome = providers.Factory(DriverFactory().chrome_driver)
    Firefox = providers.Factory(DriverFactory().firefox_driver)
    ChromeHeadLess = providers.Factory(DriverFactory().chromeheadless_driver)
    #Remote = providers.Factory(webdriver.Remote())




if __name__ == "__main__":
    print(os.getcwd())
    #driver = DriverService.ChromeHeadLess()
    #driver.get("http://www.google.com.tw")
