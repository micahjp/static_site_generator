from blocks import markdown_to_blocks
from blocks import block_to_block_type
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


class TestBlockToBlockType(unittest.TestCase):
    def test_headings(self):
        heading = "# this is a heading"

        self.assertEqual(block_to_block_type(heading), "heading")

    def test_code(self):
        code = "```this is a code block```"

        self.assertEqual(block_to_block_type(code), "code")

    def test_quote(self):
        quote = ">This is a quote block\n>every line must start with a >\n> character"

        self.assertEqual(block_to_block_type(quote), "quote")

    def test_unordered_list(self):
        unordered_list = "* this is an unordered list block\n* every line must\n* start with an astrik\n* or a hyphen and a space"
        unordered_list1 = "- this is also an unordered \n- list block, but this\n- one starts with a hyphen\n- instead of an astrik"

        self.assertEqual(block_to_block_type(unordered_list), "unordered_list")
        self.assertEqual(block_to_block_type(unordered_list1), "unordered_list")

    def test_ordered_list(self):
        ordered_list = "1. this is an ordered list\n2. each line must start with\n3. a number\n4. (starting with 1 and incrimenting by 1), a period,\n5. and a space"

        self.assertEqual(block_to_block_type(ordered_list), "ordered_list")

    def test_paragraph(self):
        paragraphs = [
                "this is a normal paragragh,\njust text, no formating\nparagraphs are used often"
                "1. this is a paragraph\n3. since the numbers\n2. do not incriment by\n4. one each time",
                "* this is a paragraph\n- because a mix of astriks\n- and hyphens are used\n* which is bad formatting",
                ">this is a paragraph\n >because this line starts with a space\n>instead of a > sign"
                ]

        for paragraph in paragraphs:
            self.assertEqual(block_to_block_type(paragraph), "paragraph")
