from textnode import TextNode
from split_nodes import split_nodes_delimiter
from split_nodes import split_nodes_image
from split_nodes import split_nodes_link
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



class TestSplitNodesImage(unittest.TestCase):
    def test_good_format(self):
        nodes = [
                TextNode("normal text ![alt text](/path/to/image)", "text"),
                TextNode("![alt text](/path/to/img) normal text", "text"),
                TextNode("![alt text img1](/path/to/img1)![alt text img2](/path/to/img2)", "text"),
                TextNode("[hyperlinked text](https://link/to/website) normal text ![alt image text](/path/to/image)", "text"),
                TextNode("normal text ![alternate image](/path/to/image) normal text", "text")
            ]
        self.assertEqual(
                split_nodes_image(nodes),
                [
                    TextNode("normal text ", "text"),
                    TextNode("alt text", "image", "/path/to/image"),
                    TextNode("alt text", "image", "/path/to/img"),
                    TextNode(" normal text", "text"),
                    TextNode("alt text img1", "image", "/path/to/img1"),
                    TextNode("alt text img2", "image", "/path/to/img2"),
                    TextNode("[hyperlinked text](https://link/to/website) normal text ", "text"),
                    TextNode("alt image text", "image", "/path/to/image"),
                    TextNode("normal text ", "text"),
                    TextNode("alternate image", "image", "/path/to/image"),
                    TextNode(" normal text", "text")
                ]
            )

    def test_bad_format(self):
        nodes = [
                TextNode("[hyperlink](https://link/to/website)!normal text", "text"),
                TextNode("![alternate text(/path/to/image)] normal text", "text"),
                TextNode("![alt text](/path/to/image)", "image"),
                TextNode("**bold text**", "bold"),
                TextNode("!alternate text]/path/to/image) nomal text", "text"),
            ]
        self.assertEqual(nodes, nodes)



class TestSplitNodesLink(unittest.TestCase):
    def test_good_format(self):
        nodes = [
                TextNode("normal text [link text](https://link-to-somewhere)", "text"),
                TextNode("[link text](https://link-to-somewhere) normal text", "text"),
                TextNode("[hyperlinked text](https://link/to/somewhere)[another hyperlink](https://link/to/nowhere)", "text"),
                TextNode("[linked text](https://link/url) normal text [hyperlink](https://link/2/)", "text")
            ]

        self.assertEqual(
                split_nodes_link(nodes),
                [
                    TextNode("normal text ", "text"),
                    TextNode("link text", "link", "https://link-to-somewhere"),
                    TextNode("link text", "link", "https://link-to-somewhere"),
                    TextNode(" normal text", "text"),
                    TextNode("hyperlinked text", "link", "https://link/to/somewhere"),
                    TextNode("another hyperlink", "link", "https://link/to/nowhere"),
                    TextNode("linked text", "link", "https://link/url"),
                    TextNode(" normal text ", "text"),
                    TextNode("hyperlink", "link", "https://link/2/")
                ]
            )

    def test_bad_format(self):
        nodes = [
                TextNode("normal text ![alt text](/path/to/image)", "text"),
                TextNode("[linked text(https://link-to-image)", "text"),
                TextNode("(https://link/test/)[bad format]", "text"),
                TextNode("normal text unlinked text](https://link/to/nothing", "text"),
                TextNode("![alt text](/path/to/an/image)", "image")
            ]

        self.assertEqual(
            split_nodes_link(nodes),
            nodes
            )
