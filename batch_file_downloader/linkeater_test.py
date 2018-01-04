import unittest;
from linkeater import LinkEater,NoLinkException

class TestLinkEater(unittest.TestCase):
    def test_read_from_source(self):
        e = LinkEater("test.txt");
        e.read_from_source();
        self.assertEqual(len(e.files),4);

    def test_empty_file(self):
        e = LinkEater("test_empty.txt");
        self.assertRaises(NoLinkException,e.read_from_source);