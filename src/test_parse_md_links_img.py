from parse_md_links_img import extract_markdown_links
from parse_md_links_img import extract_markdown_images
import unittest


class TestParseMDLinksImages(unittest.TestCase):
    def test_link_good_format(self):
        self.assertEqual(
                extract_markdown_links("normal text [hyperlinked text](https://link) more normal text [this is a hyperlink](https://url/link)"),
                [
                    ("hyperlinked text", "https://link"),
                    ("this is a hyperlink", "https://url/link")
                ])

    def test_link_bad_format(self):
        self.assertEqual(
                extract_markdown_links("normal text [hyperlink](https://link normal text [hyperlink(https://link.url"),
                []
                )

    def test_img_good_format(self):
        self.assertEqual(
                extract_markdown_images("![alt text](https://link-to-image/image.jpeg) normal text ![more alt text](https://link-to-image/image.png) more normal text"),
                [
                    ("alt text", "https://link-to-image/image.jpeg"),
                    ("more alt text", "https://link-to-image/image.png")
                ])

    def test_img_bad_format(self):
        self.assertEqual(
                extract_markdown_images("normal text [alt text](https://link-to-image/image.png)"),
                []
                )
        self.assertEqual(
                extract_markdown_images("normal text ![alt text](https://link-to-image/image.png"),
                []
                )
