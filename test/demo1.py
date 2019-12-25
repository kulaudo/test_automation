# encoding = 'utf-8'
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import unittest, time, logging, traceback, ddt

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s,[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='e://DataDrivenTesting/report.log',
    filemode='w'
)

@ddt.ddt
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='E:\\chromedriver.exe')

    @ddt.data(['America', 'WashiontonD.C.'],
        ['Japan', 'Tokyo'],
        ['Taiwan', 'Taipei'])
    @ddt.unpack
    def test_data_driven_obj(self, testdata, expectdata):
        url = "http://www.google.com"
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_name('q').send_keys(testdata)
            self.driver.find_element_by_name('btnK').click()
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException:
            logging.error('the element not found, traceback: ' + str(traceback.format_exc()))
        except ElementNotInteractableException:
            logging.error('the element not interactable, traceback: ' + str(traceback.format_exc()))
        except AssertionError:
            logging.info("search:{}, expect:{}, Failed".format(testdata, expectdata))
        except Exception:
            logging.info("Unknown Error:" + str(traceback.format_exc()))
        else:
            logging.info("Search:{}, Except:{} Passed".format(testdata, expectdata))
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


