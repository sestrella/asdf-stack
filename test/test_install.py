from lib.github_client import GithubClient
from lib.install import install

import logging
import os.path
import subprocess
import tempfile
import unittest

class TestInstall(unittest.TestCase):
  def setUp(self):
    logger = logging.getLogger('install')
    logger.setLevel(logging.NOTSET)

  def test_install_2_3_1(self):
    with tempfile.TemporaryDirectory() as install_dir:
      client = GithubClient()
      install(client, install_dir, '2.3.1')
      output = subprocess.check_output([f'{install_dir}/bin/stack', '--version'])
      self.assertIn(b'2.3.1', output)

  def test_install_1_1_2(self):
    with tempfile.TemporaryDirectory() as install_dir:
      client = GithubClient()
      install(client, install_dir, '1.1.2')
      output = subprocess.check_output([f'{install_dir}/bin/stack', '--version'])
      self.assertIn(b'1.1.2', output)
