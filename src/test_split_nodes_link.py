from textnode import TextNode
from split_nodes import split_nodes_link
import unittest


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
                    TextNode("[link text](https://link-to-somewhere)", "link", "https://link-to-somewhere"),
                    TextNode("[link text](https://link-to-somewhere)", "link", "https://link-to-somewhere"),
                    TextNode(" normal text", "text"),
                    TextNode("[hyperlinked text](https://link/to/somewhere)", "link", "https://link/to/somewhere"),
                    TextNode("[another hyperlink](https://link/to/nowhere)", "link", "https://link/to/nowhere"),
                    TextNode("[linked text](https://link/url)", "link", "https://link/url"),
                    TextNode(" normal text ", "text"),
                    TextNode("[hyperlink](https://link/2/)", "link", "https://link/2/")
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
