from main import text_to_textnode
from textnode import TextNode
import unittest


class TestTextToTextNode(unittest.TestCase):
    def test_all_types(self):
        string = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        self.assertEqual(
                text_to_textnode(string),
                [
                    TextNode("This is ", "text"),
                    TextNode("text", "bold"),
                    TextNode(" with an ", "text"),
                    TextNode("italic", "italic"),
                    TextNode(" word and a ", "text"),
                    TextNode("code block", "code"),
                    TextNode(" and an ", "text"),
                    TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", "text"),
                    TextNode("link", "link", "https://boot.dev")
                ]
            )
