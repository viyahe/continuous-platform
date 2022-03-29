from dummy.createDummy import handler
from platform_common import BaseDynamoDBTest


class TestCreateDummyHandler(BaseDynamoDBTest):
    def setUp(self):
        BaseDynamoDBTest.setUp(self)
        self.handler = handler

    def test_create_dummy(self):
        event = {'input': '?'}
        response = self.handler(event, self.context)
        self.assertTrue(response)
