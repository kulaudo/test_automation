import dependency_injector.containers as containers
import dependency_injector.providers as providers
from testauto.factory.DriverFactory import DriverFactory
import os

class DriverService(containers.DeclarativeContainer):

    Chrome = providers.Factory(DriverFactory().chrome_driver)
    Firefox = providers.Factory(DriverFactory().firefox_driver)
    ChromeHeadLess = providers.Factory(DriverFactory().chromeheadless_driver)
    #Remote = providers.Factory(webdriver.Remote())


if __name__ == "__main__":
    driver = DriverService.Chrome()
    driver.get("http://www.google.com.tw")
