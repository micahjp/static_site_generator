from markdown_conversions import markdown_to_blocks, markdown_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode
import unittest


markdown_text = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item


This is a paragraph with too many new lines



This is the final paragraph'''


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):

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


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_markdown_to_html_node(self):
        self.assertEqual(
                markdown_to_html_node(markdown_text),
                ParentNode("div", [
                        ParentNode("h1", [LeafNode(None, "This is a heading", None)]),
                        ParentNode("p", [
                            LeafNode(None, "This is a paragraph of text. It has some "),
                            LeafNode("b", "bold"),
                            LeafNode(None, " and "),
                            LeafNode("i", "italic"),
                            LeafNode(None, " words inside of it."),
                            ]),
                        ParentNode("ul", [
                            ParentNode("li", [LeafNode(None, "This is the first list item in a list block")]),
                            ParentNode("li", [LeafNode(None, "This is a list item")]),
                            ParentNode("li", [LeafNode(None, "This is another list item")])
                            ]),
                        LeafNode("p", "This is a paragraph with too many new lines"),
                        LeafNode("p", "This is the final paragraph")
                    ])
            )
