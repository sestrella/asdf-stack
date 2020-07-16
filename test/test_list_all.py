from lib.github_client import GithubClient
from lib.list_all import list_all
from unittest.mock import Mock
from pathlib import Path

import json
import unittest

class TestListAll(unittest.TestCase):
  def test_list_all(self):
    client = GithubClient()
    client.list_repo_tags = Mock(return_value=self.__read_json('./test/fixtures/tags.json'))
    printer = Mock()
    list_all(client, printer)
    printer.assert_called_once_with(' '.join([
      '1.1.2',
      '1.2.0',
      '1.3.0',
      '1.3.2',
      '1.4.0',
      '1.5.0-rc1',
      '1.5.0',
      '1.5.1',
      '1.6.0.20171017',
      '1.6.0.20171022',
      '1.6.0.20171202',
      '1.6.1',
      '1.6.1.1',
      '1.6.3',
      '1.6.3.1',
      '1.6.5',
      '1.7.0.1',
      '1.7.0.3',
      '1.7.1',
      '1.9.0.1',
      '1.9.1',
      '1.9.1.1',
      '1.9.3',
      '1.9.3.1',
      '2.1.0.1',
      '2.1.0.3',
      '2.1.1',
      '2.1.3',
      '2.3.0.1',
      '2.3.1'
  ]))

  def __read_json(self, path):
    with open(path, 'r') as file:
      return json.loads(file.read())
