from leafnode import LeafNode
import unittest


class TestLeafNode(unittest.TestCase):
    def test_new_instance(self):
        with self.assertRaises(TypeError):
            LeafNode("a", "This is a test", "Children aren't allowed", {"key": "value"})

        with self.assertRaises(TypeError):
            LeafNode()

        node = LeafNode(None, "This is a test")
        node1 = LeafNode("a", "This is a test")

        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, "This is a test")

        self.assertEqual(node1.tag, "a")
        self.assertEqual(node1.value, "This is a test")

    def test_to_html(self):
        node = LeafNode("a", None)

        with self.assertRaises(ValueError):
            node.to_html()

        node1 = LeafNode("a", "This is a test")
        node2 = LeafNode("a", "This is a test", {"href": "http://test.com", "type": "test"})
        node3 = LeafNode(None, "This is a test")

        self.assertEqual(node1.to_html(), "<a>This is a test</a>")
        self.assertEqual(node2.to_html(), '<a href="http://test.com" type="test">This is a test</a>')
        self.assertEqual(node3.to_html(), "This is a test")
