import dependency_injector.providers as providers
from selenium import webdriver
from enum import Enum, auto
from selenium.webdriver.chrome.options import Options
import configparser
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver_config = configparser.ConfigParser()
driver_config.read('../../../webdriver.ini')

class DriverFactory:
    
    def chrome_driver(self):
        return webdriver.Chrome(executable_path=driver_config['Chrome']['Path'])

    def firefox_driver(self):
        return webdriver.Firefox(executable_path=driver_config['Firefox']['Path'])

    def chromeheadless_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        return webdriver.Chrome(executable_path=driver_config['Chrome Headless']['Path'], options=chrome_options)

    def remote_chrome_driver(self):
        return webdriver.Remote(
            command_executor=driver_config['Remote Default Chrome']['command_executor'],
            desired_capabilities=DesiredCapabilities.CHROME)

    def remote_firfox_driver(self):
        return webdriver.Remote(
            command_executor=driver_config['Remote Default Firefox']['command_executor'],
            desired_capabilities=DesiredCapabilities.FIREFOX)

    def remote_ie_driver(self):
        return webdriver.Remote(
            command_executor=driver_config['Remote Default IE']['command_executor'],
            desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
            
