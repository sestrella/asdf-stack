from lib.install import install

import subprocess
import tempfile
import unittest


class TestInstall(unittest.TestCase):
    def test_install_2_5(self):
        with tempfile.TemporaryDirectory() as install_dir:
            stack_bin = install(install_dir, '2.5.1')
            output = subprocess.check_output([stack_bin, '--version'])
            self.assertIn(b'2.5.1', output)

    def test_install_2_3(self):
        with tempfile.TemporaryDirectory() as install_dir:
            stack_bin = install(install_dir, '2.3.3')
            output = subprocess.check_output([stack_bin, '--version'])
            self.assertIn(b'2.3.3', output)

    def test_install_1_1(self):
        with tempfile.TemporaryDirectory() as install_dir:
            stack_bin = install(install_dir, '1.1.2')
            output = subprocess.check_output([stack_bin, '--version'])
            self.assertIn(b'1.1.2', output)
