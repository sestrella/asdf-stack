from lib.github_client import GithubClient
from lib.list_all import list_all
from unittest.mock import Mock

import unittest

class TestListAll(unittest.TestCase):
  def test_list_all(self):
    client = GithubClient('secret')
    client.list_repo_tags = Mock(return_value=[{
      'name': 'v2.3.1'
    }, {
      'name': 'v2.3.0.1'
    }])
    printer = Mock()

    list_all(client, printer)

    printer.assert_called_once_with('2.3.0.1 2.3.1')
