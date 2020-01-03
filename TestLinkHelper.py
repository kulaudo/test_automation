import testlink

class MyTestlinkHelper(object):
    def __init__(self, client):
        self.client = client
        
    def get_automated_tests_from_testplan_id(testplan_id):
        return [y for y in [ self.client.getTestCase(x)[0] for x in self.client.getTestCasesForTestPlan(testplan_id).keys()] if y['execution_type']=='2']