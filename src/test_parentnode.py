from parentnode import ParentNode
from leafnode import LeafNode
import unittest


class TestParentNode(unittest.TestCase):
    def test_new_instance(self):
        with self.assertRaises(TypeError):
            ParentNode()
        with self.assertRaises(TypeError):
            ParentNode("a")

    def test_to_html(self):
        node = ParentNode(
                "ul",
                [
                    LeafNode("li", "bananas"),
                    LeafNode("li", "apples"),
                    LeafNode("li", "pear"),
                    LeafNode("li", "flour"),
                    ParentNode("li", [LeafNode("b", "eggs")])
                ]
        )
        self.assertEqual(
                node.to_html(),
                "<ul><li>bananas</li><li>apples</li><li>pear</li><li>flour</li><li><b>eggs</b></li></ul>"
                )

        node1 = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node1.to_html()
