import io
import lib.list_all
import unittest
import unittest.mock

class TestListAll(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_all(self, mock_stdout):
        lib.list_all.list_all()
        self.assertIn('2.1.1 2.1.3', mock_stdout.getvalue())

    def test_list_tags(self):
        tags = lib.list_all.list_tags()
        self.assertTrue(len(tags) > 0)

    def test_tags_to_versions(self):
        versions = lib.list_all.tags_to_versions([
            { 'name': 'v2.1.3' },
            { 'name': 'v2.1.1' }
        ])
        self.assertEqual(versions, '2.1.1 2.1.3')
