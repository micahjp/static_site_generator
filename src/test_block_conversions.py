from block_conversions import block_to_block_type, block_to_children, block_to_htmlnode
from leafnode import LeafNode
import unittest


class TestBlockToBlockType(unittest.TestCase):
    def test_headings(self):
        h1 = "# this is a heading"
        h2 = "## this is a heading"
        h3 = "### this is a heading"
        h4 = "#### this is a heading"
        h5 = "##### this is a heading"
        h6 = "###### this is a heading"
        bad_format = "#x#b# this is an invalid format which ends up as a paragraph"

        self.assertEqual(block_to_block_type(h1), "heading")
        self.assertEqual(block_to_block_type(h2), "heading")
        self.assertEqual(block_to_block_type(h3), "heading")
        self.assertEqual(block_to_block_type(h4), "heading")
        self.assertEqual(block_to_block_type(h5), "heading")
        self.assertEqual(block_to_block_type(h6), "heading")
        self.assertEqual(block_to_block_type(bad_format), "paragraph")

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


class TestBlockToChildren(unittest.TestCase):
    def test_many_children(self):
        block = "This is text with a **bold** word, an *italic* word and a `code block`, as well as an ![image](https://path/to/image) and a [link](https://link/to/somewhere)"

        self.assertEqual(
                block_to_children(block, block_to_block_type(block)),
                [
                    LeafNode(None, "This is text with a ", None),
                    LeafNode("b", "bold", None),
                    LeafNode(None, " word, an ", None),
                    LeafNode("i", "italic", None),
                    LeafNode(None, " word and a ", None),
                    LeafNode("code", "code block", None),
                    LeafNode(None, ", as well as an ", None),
                    LeafNode("img", "", {'src': 'https://path/to/image', 'alt': 'image'}),
                    LeafNode(None, " and a ", None),
                    LeafNode("a", "link", {'href': 'https://link/to/somewhere'})
                ]
            )
