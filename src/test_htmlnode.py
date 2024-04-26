import unittest
from htmlnode import (HTMLNode, LeafNode, ParentNode)


class TestHTMLNode(unittest.TestCase):
    def test_node_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_leaf_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_repr(self):
        node = LeafNode("p", "Hello, world!", {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(
            "LeafNode(p, Hello, world!, {'class': 'greeting', 'href': 'https://boot.dev'})",
            repr(node),
        )


    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_to_html_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("p", "Hello, world!")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_to_html(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "Hello, world!"), LeafNode("p", "Another paragraph!")],
        )
        self.assertEqual(
            node.to_html(), "<div><p>Hello, world!</p><p>Another paragraph!</p></div>"
        )

    def test_parent_repr(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "Hello, world!"), LeafNode("p", "Another paragraph!")],
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            "ParentNode(div, children: [LeafNode(p, Hello, world!, None), LeafNode(p, Another paragraph!, None)], {'class': 'greeting', 'href': 'https://boot.dev'})",
            repr(node),
        )

if __name__ == "__main__":
    unittest.main()