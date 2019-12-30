import dependency_injector.containers as containers
import dependency_injector.providers as providers
from testauto.factory.DriverFactory import DriverFactory, ChromeDriverFactory, ChromeDriverConfig, RemoteChromeDriverConfig, RemoteChromeDriverFactory, RemoteFirefoxDriverFactory, RemoteFirefoxDriverConfig, FirefoxDriverFactory,FirefoxDriverConfig
import os

class DriverService(containers.DeclarativeContainer):

    
    Chrome = providers.Factory(
        ChromeDriverFactory(ChromeDriverConfig('../../../webdriver.ini')).create_driver)

    Firefox = providers.Factory(
        FirefoxDriverFactory(FirefoxDriverConfig('../../../webdriver.ini')).create_driver)

    RemoteChrome = providers.Factory(RemoteChromeDriverFactory(
        RemoteChromeDriverConfig('../../../webdriver.ini')).create_driver)

    RemoteFirefox = providers.Factory(RemoteFirefoxDriverFactory(
        RemoteFirefoxDriverConfig('../../../webdriver.ini')).create_driver)
    # old
    # Firefox = providers.Factory(DriverFactory().firefox_driver)
    # ChromeHeadLess = providers.Factory(DriverFactory().chromeheadless_driver)
    # Remote = providers.Factory(webdriver.Remote())


if __name__ == "__main__":
    driver = DriverService.Firefox()
    driver.get("http://www.google.com.tw")
    driver.quit()
    driver = DriverService.Chrome()
    driver.get("http://www.google.com.tw")
    driver.quit()
