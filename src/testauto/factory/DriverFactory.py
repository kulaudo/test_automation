import typing
import dependency_injector.providers as providers
from selenium import webdriver
from enum import Enum, auto
from selenium.webdriver.chrome.options import Options
import configparser
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import abc


class WebDriverConfig(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def get_webdriver_executable_path(self):
        pass

class RemoteWebDriverConfig(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_remote_webdriver_command_executor(self):
        pass

    @abc.abstractmethod
    def get_remote_webdriver_desired_capabilities(self):
        pass


class ChromeDriverConfig(WebDriverConfig):
    def __init__(self, path):
        
        self.driver_config = configparser.ConfigParser()
        self.driver_config.read(path)
    
    def get_webdriver_executable_path(self):
        return self.driver_config['Chrome']['Path']


class FirefoxDriverConfig(WebDriverConfig):
    def __init__(self, path):
        self.driver_config = configparser.ConfigParser()
        self.driver_config.read(path)
        
    def get_webdriver_executable_path(self):
        return self.driver_config['Firefox']['Path']


class RemoteChromeDriverConfig(RemoteWebDriverConfig):

    def __init__(self, path):
        self.remote_driver_config = configparser.ConfigParser()
        self.remote_driver_config.read(path)

    def get_remote_webdriver_command_executor(self):
        return self.remote_driver_config['Remote Default Chrome']['command_executor']

    def get_remote_webdriver_desired_capabilities(self):
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['platform'] = self.remote_driver_config['Remote Default Chrome']['platform']        
        capabilities['version'] = self.remote_driver_config['Remote Default Chrome']['version']
        capabilities['browserName'] = self.remote_driver_config['Remote Default Chrome']['browserName']
        return capabilities
            
        


class RemoteFirefoxDriverConfig(RemoteWebDriverConfig):

    def __init__(self, path):
        self.remote_driver_config = configparser.ConfigParser()
        self.remote_driver_config.read(path)

    def get_remote_webdriver_command_executor(self):
        return self.remote_driver_config['Remote Default Firefox']['command_executor']

    def get_remote_webdriver_desired_capabilities(self):
        capabilities = DesiredCapabilities.FIREFOX
        #capabilities['platform'] = self.remote_driver_config['Remote Default Firefox']['platform']
        #capabilities['version'] = self.remote_driver_config['Remote Default Firefox']['version']
        #capabilities['browserName'] = self.remote_driver_config['Remote Default Firefox']['browserName']
        return capabilities


class AbstractDriverFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_driver(self):
        pass


class ChromeDriverFactory(AbstractDriverFactory):

    def __init__(self, driver_config: WebDriverConfig):
        self.driver_config = driver_config

    def create_driver(self):
        return webdriver.Chrome(executable_path=self.driver_config.get_webdriver_executable_path())


class FirefoxDriverFactory(AbstractDriverFactory):

    def __init__(self, driver_config: WebDriverConfig):
        self.driver_config = driver_config

    def create_driver(self):
        return webdriver.Firefox(executable_path=self.driver_config.get_webdriver_executable_path())


class RemoteChromeDriverFactory(AbstractDriverFactory):
    def __init__(self, remote_driver_config: RemoteWebDriverConfig):
        self.remote_driver_config = remote_driver_config

    def create_driver(self):
        return webdriver.Remote(
            command_executor=self.remote_driver_config.get_remote_webdriver_command_executor(),
            desired_capabilities=DesiredCapabilities.CHROME)


class RemoteFirefoxDriverFactory(AbstractDriverFactory):
    def __init__(self, remote_driver_config: RemoteWebDriverConfig):
        self.remote_driver_config = remote_driver_config

    def create_driver(self):
        return webdriver.Remote(
            command_executor=self.remote_driver_config.get_remote_webdriver_command_executor(),
            #desired_capabilities=self.remote_driver_config.get_remote_webdriver_desired_capabilities())
            desired_capabilities=DesiredCapabilities.FIREFOX)


class DriverFactory:

    def __init__(self, driver_config):
        self.driver_config = configparser.ConfigParser()
        self.driver_config.read('../../../webdriver.ini')
    
    def chrome_driver(self):
        return webdriver.Chrome(executable_path=self.driver_config['Chrome']['Path'])

    def firefox_driver(self):
        return webdriver.Firefox(executable_path=self.driver_config['Firefox']['Path'])

    def chromeheadless_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        return webdriver.Chrome(executable_path=self.driver_config['Chrome Headless']['Path'], options=chrome_options)

    def remote_chrome_driver(self):
        return webdriver.Remote(
            command_executor=self.driver_config['Remote Default Chrome']['command_executor'],
            desired_capabilities=DesiredCapabilities.CHROME)

    def remote_firfox_driver(self):
        return webdriver.Remote(
            command_executor=self.driver_config['Remote Default Firefox']['command_executor'],
            desired_capabilities=DesiredCapabilities.FIREFOX)

    def remote_ie_driver(self):
        return webdriver.Remote(
            command_executor=self.driver_config['Remote Default IE']['command_executor'],
            desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)


