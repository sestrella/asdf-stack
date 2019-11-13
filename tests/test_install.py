import lib.install
import os
import tempfile
import unittest

class TestInstall(unittest.TestCase):
    #def test_release_by_tag(self):
    #    release = lib.install.release_by_tag(
    #        'commercialhaskell',
    #        'stack',
    #        'v2.1.3'
    #    )
    #    self.assertEqual(release['tag_name'], 'v2.1.3')

    def test_assets_by_content_type(self):
        urls = list(lib.install.assets_by_content_type([
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

    def test_urls_by_type(self):
        self.assertEqual(
            lib.install.urls_by_type([
                'stack-2.1.3-linux-x86_64-static.tar.gz',
                'stack-2.1.3-linux-x86_64.tar.gz'
            ]),
            {
                'static': 'stack-2.1.3-linux-x86_64-static.tar.gz',
                'default': 'stack-2.1.3-linux-x86_64.tar.gz'
            }
        )
        self.assertEqual(
            lib.install.urls_by_type([
                'stack-1.9.3-linux-x86_64-gmp4.tar.gz',
                'stack-1.9.3-linux-x86_64-static.tar.gz',
                'stack-1.9.3-linux-x86_64.tar.gz'
            ]),
            {
                'gmp4': 'stack-1.9.3-linux-x86_64-gmp4.tar.gz',
                'static': 'stack-1.9.3-linux-x86_64-static.tar.gz',
                'default': 'stack-1.9.3-linux-x86_64.tar.gz'
            }
        )

    def test_foo(self):
        self.assertEqual(
            lib.install.foo({
                'static': 'stack-2.1.3-linux-x86_64-static.tar.gz',
                'default': 'stack-2.1.3-linux-x86_64.tar.gz'
            }),
            'stack-2.1.3-linux-x86_64-static.tar.gz'
        )
        self.assertEqual(
            lib.install.foo({
                'gmp4': 'stack-1.7.1-linux-x86_64-gmp4.tar.gz',
                'default': 'stack-1.7.1-linux-x86_64.tar.gz'
            }),
            'stack-1.7.1-linux-x86_64.tar.gz'
        )

    def test_download_and_extract(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = lib.install.download_and_extract(
                'https://github.com/commercialhaskell/stack/releases/download/v2.1.3/stack-2.1.3-linux-x86_64-static.tar.gz',
                tmp
            )
            self.assertEqual(path, f"{tmp}/stack-2.1.3-linux-x86_64-static")
