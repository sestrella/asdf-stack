from lib.list_all import list_all
from unittest.mock import Mock

import unittest


class TestListAll(unittest.TestCase):
    def test_list_all_pagination(self):
        printer = Mock()
        tags = list_all(printer)
        self.assertTrue(len(tags) >= 58)

    def test_list_all_printer(self):
        printer = Mock()
        list_all(printer)
        self.assertIn('2.3.3 2.5.0.1 2.5.1', printer.call_args[0][0])
