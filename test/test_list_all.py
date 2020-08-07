from lib.github_client import GithubClient
from lib.list_all import list_all
from pathlib import Path
from unittest.mock import Mock

import unittest

class TestListAll(unittest.TestCase):
  def test_list_all(self):
    client = GithubClient()
    printer = Mock()
    list_all(client, printer)
    self.assertIn('2.3.1', printer.call_args.args[0])
