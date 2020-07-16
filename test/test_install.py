from lib.github_client import GithubClient
from lib.install import install

import os.path
import unittest
import tempfile

class TestInstall(unittest.TestCase):
  def test_install(self):
    with tempfile.TemporaryDirectory() as install_dir:
      client = GithubClient()
      install(client, install_dir, '2.1.3')
      self.assertTrue(os.path.isfile(f'{install_dir}/bin/stack'))
