from textnode import TextNode
from split_nodes import split_nodes_delimiter
import unittest


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_no_closing_delimiter(self):
        node = TextNode("this is a test **this is bold text", "text")
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", "bold"),

    def test_not_text_type(self):
        node = TextNode("this is a test this is bold text", "bold")
        self.assertEqual(
                split_nodes_delimiter([node], "**", "bold"),
                [TextNode("this is a test this is bold text", "bold")]
                )

    def test_starts_with_delimiter(self):
        node = TextNode("`code snippet` normal text", "text")

        self.assertEqual(
                split_nodes_delimiter([node], "`", "code"),
                [TextNode("code snippet", "code"), TextNode(" normal text", "text")]
                )

    def test_ends_with_delimiter(self):
        node = TextNode("normal text `code snippet`", "text")

        self.assertEqual(
                split_nodes_delimiter([node], "`", "code"),
                [TextNode("normal text ", "text"), TextNode("code snippet", "code")]
                )

    def test_no_delimiter(self):
        node = TextNode("normal text normal text", "text")

        self.assertEqual(
                split_nodes_delimiter([node], "*", "italic"),
                [node]
                )

    def test_multi_nodes(self):
        node = TextNode("*italic text* normal text", "text")
        node1 = TextNode("normal text *italic text* normal text", "text")
        node2 = TextNode("bold text", "bold")
        node3 = TextNode("normal text *italic text*", "text")

        nodes = [node, node1, node2, node3]

        self.assertEqual(
                split_nodes_delimiter(nodes, "*", "italic"),
                [
                    TextNode("italic text", "italic"),
                    TextNode(" normal text", "text"),
                    TextNode("normal text ", "text"),
                    TextNode("italic text", "italic"),
                    TextNode(" normal text", "text"),
                    TextNode("bold text", "bold"),
                    TextNode("normal text ", "text"),
                    TextNode("italic text", "italic")
                ]
                )
