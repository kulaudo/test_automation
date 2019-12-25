# encoding = 'utf-8'
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
import logging
import traceback
import ddt
import testauto.ExcelUtil
import sys
import os
import dependency_injector.errors
from testauto.factory.DriverFactory import DriverService


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s,[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='e://DataDrivenTesting/report.log',
    filemode='a'
)
excel_path = 'E:\\test_automation\\test\\test_data\\test_sheet.xlsx'
sheet_name = 'search_data'
excel = testauto.ExcelUtil.ParseExcel(excel_path, sheet_name)


@ddt.ddt 
class TestDemo(unittest.TestCase):
    
    
    def setUp(self):
        self.driver = None
        self.err_logger = logging.getLogger("Error")
        self.fail_logger = logging.getLogger('Failure')
        
        fh = logging.FileHandler('error.log')
        formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s','%Y-%m-%d %H:%M:%S')        
        fh.setFormatter(formatter)
        
        self.err_logger = logging.getLogger('ExcetionError')
        self.err_logger.addHandler(fh)
        try:
            url = "http://www.google.com.tw"
            self.driver = DriverService.ChromeHeadLess()
            self.driver.implicitly_wait(10)
            self.driver.get(url)
        except dependency_injector.errors.Error as e:
            self.err_logger.error('dependency_injector error:' + traceback.format_exc())
        except Exception as e:
            self.err_logger.error('error occured in setup:',traceback.format_exc())
            raise InterruptedError("Cannot setUp test!!")

    
    @ddt.idata(excel.get_data_from_sheet())
    def test_data_driver_by_file(self, file_data):      
        testdata, expectdata = file_data[1],file_data[2]
        
        try:            
            self.driver.find_element_by_name('c').send_keys(testdata)
            self.driver.find_element_by_name('btnK').click()
            time.sleep(5)
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException as e:
            logging.error(traceback.format_exc())
        except AssertionError:
            logging.error("[Fail] search:{}, expect:{}".format(testdata, expectdata))
        except Exception as e:
            logging.error(traceback.format_exc())
        else:
            logging.info("[Pass] Search:{}, Except:{}".format(testdata, expectdata))
    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()


