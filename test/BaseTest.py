import unittest
from testauto.factory.DriverFactory import DriverService
from page_objects.page_objects import PageElement,PageObject,MultiPageElement
import time
import ddt
import logging
from functools import wraps

class logger(object):
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.info("[{level}]: the function {func}() is running..."\
                .format(level=self.level, func=func.__name__))
            func(*args, **kwargs)


def use_logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('{} is running'.format(func.__name__))
        func(*args, **kwargs)
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1=time.time()
        func(*args, **kwargs)
        t2=time.time()
        logging.info("{} time spent：{} sec".format(func.__name__,t2-t1))
    return wrapper

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = DriverService.Chrome()

    def tearDown(self):
        self.driver.quit()
        


@ddt.ddt
class LoginTest(BaseTest):
   
    def __init__(self, methodName):
        super().__init__(methodName)
        

    def test_get_page(self):
        page = PageObject(webdriver=self.driver)
        page.get("http://www.google.com")

    def test_login_using_page_object(self):               
        class MyPage(PageObject):
            elem1 = PageElement(id_='Account')
            elem2 = PageElement(id_='Password')
        page = MyPage(webdriver=self.driver)
        page.get("http://192.168.50.178:5001")
        page.elem1.send_keys('director1')
        page.elem2.send_keys('123fff')
        time.sleep(3)
    
    @use_logging
    @ddt.data(('Account', 'Password'))    
    def test_login_using_page_object_ddt(self, value):
        id1,id2 = value
        class MyPage(PageObject):
            elem1 = PageElement(id_='Account')
            elem2 = PageElement(id_='Password')
        page = MyPage(webdriver=self.driver)
        page.get("http://192.168.50.178:5001")
        page.elem1.send_keys('director1')
        page.elem2.send_keys('123fff')
        time.sleep(3)



    

        

