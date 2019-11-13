import lib.install
import os
import subprocess
import tempfile
import unittest

class TestInstall(unittest.TestCase):
    def test_install(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            stack_bin = lib.install.install(tmpdir, '2.1.3')
            version = subprocess.check_output([stack_bin, '--version'])
            self.assertIn(b'2.1.3', version)

    def test_release_by_tag(self):
        release = lib.install.release_by_tag('v2.1.3')
        self.assertEqual(release['tag_name'], 'v2.1.3')

    def test_tarball_assets(self):
        urls = list(lib.install.tarball_assets([
            {
                'content_type': 'application/x-tgz',
                'browser_download_url': 'stack.tar.gz'
            },
            {
                'content_type': 'application/zip',
                'browser_download_url': 'stack.zip'
            }
        ]))
        self.assertEqual(urls, ['stack.tar.gz'])

    def test_url_by_type(self):
        self.assertEqual(
            lib.install.url_by_type([
                'stack-1.9.3-linux-x86_64-gmp4.tar.gz',
                'stack-1.9.3-linux-x86_64-static.tar.gz',
                'stack-1.9.3-linux-x86_64.tar.gz'
            ]),
            'stack-1.9.3-linux-x86_64-static.tar.gz',
        )
        self.assertEqual(
            lib.install.url_by_type([
                'stack-1.7.1-linux-x86_64-gmp4.tar.gz',
                'stack-1.7.1-linux-x86_64.tar.gz'
            ]),
            'stack-1.7.1-linux-x86_64.tar.gz',
        )

    def test_download_and_extract(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = lib.install.download_and_extract(
                'https://github.com/commercialhaskell/stack/releases/download/v2.1.3/stack-2.1.3-linux-x86_64-static.tar.gz',
                tmpdir
            )
            self.assertEqual(path, f"{tmpdir}/stack-2.1.3-linux-x86_64-static")
