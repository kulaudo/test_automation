# encoding = 'utf-8'
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time, logging, traceback, ddt

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s,[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H: %M: %S',
    filename='e://DataDrivenTesting/report.log',
    filemode='w'
)

@ddt.ddt
class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        TestDemo.trStr = ""

    def setUp(self):
        self.driver = webdriver.Firefox()

    @ddt.file_data("test_data_list.json")
    def test_data_driver_by_file(self, value):
        flag_dict = {0: 'red', 1: '#00AC4E'}
        url = "http://www.google.com"
        self.driver.get(url)
        self.driver.maximize_window()
        print(value)
        testdata, expectdata = tuple(value.strip().split('||'))
        self.driver.implicitly_wait(10)
        try:
            start = time.time()
            start_time = time.strftime(" %Y - %m - %d %H: %M: %S", time.localtime())
            self.driver.find_element_by_name('q').sendkeys(testdata)
            self.driver.find_element_by_name('btnK').click()
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException:
            logging.error('the element not found, traceback: ' + str(traceback.format_exc()))
        except AssertionError:
            logging.info("search:{}, expect:{}, Failed".format(testdata, expectdata))
        except Exception:
            logging.info("Unknown Error:" + str(traceback.format_exc()))
        else:
            logging.info("Search:{}, Except:{} Passed".format(testdata, expectdata))
        TestDemo.trStr += u'''
        <tr>
            <td> %s </td>
            <td> %s </td>
            <td> %s </td>
            <td> %.2f </td>
            <td style="color: %s"> %s </td>
        </tr><br/> % (testdata, expectdata, startTime, wasteTime, flagDict[flag], status)
        '''
        

    @classmethod
    def tearDownClass(cls):
        htmlTemplate(TestDemo.trStr)

if __name__ == "__main__":
    unittest.main()


