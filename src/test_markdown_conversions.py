from markdown_conversions import markdown_to_blocks
import unittest


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown_text = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item


This is a paragraph with too many new lines



This is the final paragraph'''

        self.assertEqual(
                markdown_to_blocks(markdown_text),
                [
                    "# This is a heading",
                    "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                    "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
                    "This is a paragraph with too many new lines",
                    "This is the final paragraph"
                ]
            )
