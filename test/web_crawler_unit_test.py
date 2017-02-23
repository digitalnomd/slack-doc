import sys
sys.path.append('../src/')

import unittest

import web_crawler as wc

class TestWebCrawler(unittest.TestCase):

    def test_getpage(self):
        page = "https://docs.python.org/2/library/functions.html#max"
        print(wc.get_page(page))
        self.assertTrue(wc.getpage(page) is not None)



    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
