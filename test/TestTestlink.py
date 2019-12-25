import testlink
import logging
import unittest
import traceback
from unittest import mock
from testlink.testlinkerrors import TLResponseError
import json


class TestTestLink(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        SERVER_URL = 'http://192.168.50.169/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
        DEV_KEY = 'ec98b68c3121de5184d2a138558764fd'
        self.client = testlink.TestLinkHelper(
            server_url=SERVER_URL, devkey=DEV_KEY).connect(testlink.TestlinkAPIClient)
        self.logger = logging.getLogger()
        

    def test_getProjectTestPlans(self):
        self.logger.info('testproject id 1={}'.format(self.client.getProjectTestPlans(testprojectid='1')))

    def test_is_working(self):
        self.assertEqual('Hello!', self.client.sayHello())

    def test_countProjects(self):
        #self.logger.info('count projects:{}'.format(self.client.countProjects()))
        self.assertEqual(5, self.client.countProjects())

    def test_countTestSuites(self):
        self.logger.info('count suites:{}'.format(self.client.countTestSuites()))

    def test_countTestCasesTP(self):
        try:
            self.logger.info('all the test cases linked to a Test Plan:{}'.format(self.client.countTestCasesTP()))
        except TLResponseError as e:            
            self.logger.error(e)
        except BaseException as e:            
            self.logger.error(e)

    def test_getProjectIDByName(self):
        try:
            self.logger.info('SSC project id = {}'.format(self.client.getProjectIDByName('SSC')))
        except TLResponseError as e:            
            self.logger.error(e)
        except BaseException as e:            
            self.logger.error(e)

    def test_getProjects(self):
        try:
            for i in self.client.getProjects():
                self.logger.info('project id : {}, name:{}'.format(i['id'],i['name']))
        except TLResponseError as e:            
            self.logger.error(e)
        except BaseException as e:            
            self.logger.error(e)

    def test_getLatestBuildForTestPlan(self):
        try:
            for i in self.client.getLatestBuildForTestPlan(4225):
                self.logger.info('testplan id : {}, name:{}'.format(i['id'],i['name']))
        except TLResponseError as e:            
            self.logger.error(e)
        except BaseException as e:            
            self.logger.error(e)

    def test_getProjectTestPlans(self):
        try:
            for i in self.client.getProjectTestPlans(4019):
                self.logger.info('testplan id for project id 4019 : {}, name:{}'.format(i['id'],i['name']))
        except TLResponseError as e:            
            self.logger.error(e)
        except BaseException as e:            
            self.logger.error(e)

    def test_getTestSuitesForTestPlan(self):
        try:
            for i in self.client.getTestSuitesForTestPlan(4225):
                self.logger.info('testsuite id :{}, name:{}'.format(i['id'],i['name']))
        except TLResponseError as e:            
            self.logger.error(e)
        except BaseException as e:            
            self.logger.error(e)
    
    def test_getLatestBuildForTestPlan(self):
        try:
            i = self.client.getLatestBuildForTestPlan(4225)
            self.logger.info('latest build id :{}, name:{}, testplan_id:{}'.format(i['id'],i['name'],i['testplan_id']))
        except TLResponseError as e:            
            self.logger.error(e)
        except BaseException as e:            
            self.logger.error("test_getLatestBuildForTestPlan",e)

    def test_getTestSuitesForTestSuite(self):
        try:
            for i in self.client.getTestSuitesForTestSuite(4077):
                self.logger.info('suite id :{}, name:{}'.format(i['id'],i['name']))
        except TLResponseError as e:            
            self.logger.error(e)
        except BaseException as e:      
            self.logger.error(e)

    def test_getTestCasesForTestPlan(self):
        try:
            i = self.client.getTestCasesForTestPlan(4225)
            self.logger.info('total test case for testplan id 4225: {}'.format( len(i)))
        except TLResponseError as e:            
            self.logger.error(e)
        except BaseException as e:      
            self.logger.error(e)

    def test_getTestCasesForTestSuite(self):
        '''
        getTestCasesForTestSuite() method of testlink.testlinkapi.TestlinkAPIClient instance
    List test suites within a test plan alphabetically

    details - default is 'simple',
              use 'full' if you want to get summary,steps & expected_results
              or 'only_id', if you just need an ID list

    deep - True/False - default is True
           if True, return also test case of child suites

    getkeywords - True/False - default is False
           if True AND details='full', dictionary includes for each test
           case, which as assigned keywords, an additional key value pair
           'keywords'

    returns an empty list, if no build is assigned
        '''
        try:            
            self.logger.info(self.client.getTestCasesForTestSuite(testsuiteid=4077,deep=True,details='only_id')[0])
        except TLResponseError as e:            
            self.logger.error(e)

    def test_getTestCase(self):
        try:            
            self.logger.info(self.client.getTestCase(self.client.getTestCasesForTestSuite(testsuiteid=4077,deep=True,details='only_id')[0]))
        except TLResponseError as e:            
            self.logger.error(e)


    def test_get_Automated_TestCase_from_TestPlan(self):
        try:
            for automated_cases in [y for y in [ self.client.getTestCase(x)[0] for x in self.client.getTestCasesForTestPlan(4225).keys()] if y['execution_type']=='2']:
                self.logger.info(automated_cases)
        except TLResponseError as e:            
            self.logger.error(e)



