from extract_and_generate_page import extract_title, generate_page
import unittest


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        string0 = "# this is a correctly formatted h1 title        "
        string1 = "this is not an h1 title and should raise an excetption"
        string2 = "# this is a good format h1 title\n\nthis is a paragraph block"

        self.assertEqual(extract_title(string0), "this is a correctly formatted h1 title")
        with self.assertRaises(Exception):
            extract_title(string1)
        self.assertEqual(extract_title(string2), "this is a good format h1 title")
