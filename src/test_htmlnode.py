import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("b", "This is a test", [], {"href": "https://test.com"})
        node1 = HTMLNode("a", "This is a test", None, None)

        self.assertEqual(
                node,
                HTMLNode("b", "This is a test", [], {"href": "https://test.com"})
                )
        self.assertNotEqual(node, node1)

    def test_repr(self):
        node = HTMLNode("p", "This is a test", [])
        node1 = HTMLNode()

        self.assertEqual(
                node.__repr__(),
                f"HTMLNode({node.tag}, {node.value}, {node.children}, {node.props})"
                )

        self.assertEqual(
                node1.__repr__(),
                f"HTMLNode({node1.tag}, {node1.value}, {node1.children}, {node1.props})"
                )

    def test_props_to_html(self):
        test_props = {
                "attribute": "value",
                "attribute1": "value1",
                "attribute2": "value2"
                     }
        node = HTMLNode(props=test_props)

        self.assertEqual(
                node.props_to_html(),
                "".join(map(lambda key: f' {key}="{test_props[key]}"', test_props))
                )
