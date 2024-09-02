from textnode import TextNode
from split_nodes import split_nodes_image
import unittest


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
