from textnode import TextNode
from leafnode import LeafNode
from text_node_conversions import text_node_to_html_node
import unittest


class TestMain(unittest.TestCase):
    def test_text_node_to_html_node(self):
        text_node = TextNode("This is a text node", "text")
        bold_node = TextNode("This is a bold node", "bold")
        italic_node = TextNode("This is a italic node", "italic")
        code_node = TextNode("This is a code node", "code")
        link_node = TextNode("This is a link node", "link", "https://link.com")
        image_node = TextNode("This is an image node", "image", "https://image.com")

        self.assertEqual(
                text_node_to_html_node(text_node),
                LeafNode(None, text_node.text)
                )
        self.assertEqual(
                text_node_to_html_node(bold_node),
                LeafNode("b", bold_node.text)
                )
        self.assertEqual(
                text_node_to_html_node(italic_node),
                LeafNode("i", italic_node.text)
                )
        self.assertEqual(
                text_node_to_html_node(code_node),
                LeafNode("code", code_node.text)
                )
        self.assertEqual(
                text_node_to_html_node(link_node),
                LeafNode("a", link_node.text, {"href": link_node.url})
                )
        self.assertEqual(
                text_node_to_html_node(image_node),
                LeafNode("img", "", {"src": image_node.url, "alt": image_node.text})
                )
