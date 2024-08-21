import unittest
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", "bold")
        node1 = TextNode("This is a test node", "bold")
        node2 = TextNode("This is a test node", "italic")

        self.assertEqual(node, node1)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a test node", "italic", "https://test.com")
        self.assertEqual(node.__repr__(), f"TextNode({node.text}, {node.text_type}, {node.url})")

    def test_default_url(self):
        node = TextNode("This is a test node", "underline")
        self.assertEqual(node.url, None)


if __name__ == "__main__":
    unittest.main()
