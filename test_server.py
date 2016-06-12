# -*- coding: utf-8 -*-
import unittest
from main import *


class TestServer(unittest.TestCase):
    TEST_FACT = 5
    TEST_RESULT = [1, 5]

    def setUp(self):
        run_server()
        self.http_handler = Handler()

    def test_factors(self):
        fact = self.http_handler.get_factors(self.TEST_FACT)
        self.assertEquals(fact, self.TEST_RESULT)

    def test_get_server_result(self):
        res = self.http_handler.get_server_result()
        self.assertTrue(res.find('html')>0)


if __name__ == '__main__':
    unittest.main()
