import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_default_url_value(self):
        node = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node.url, None)

    def test_non_eq_when_url_is_different(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_non_eq_when_text_type_is_different(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_italic)
        self.assertNotEqual(node, node2)

    def test_non_eq_when_text_is_different(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is different text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text node", text_type_text)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is a text node", text_type_bold)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "strong")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_text_node_to_html_node_italic(self):
        node = TextNode("This is a text node", text_type_italic)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "em")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_text_node_to_html_node_code(self):
        node = TextNode("This is a text node", text_type_code)
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, None)

    def test_text_node_to_html_node_link(self):
        node = TextNode("This is a text node", text_type_link, "https://www.boot.dev")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

    def test_text_node_to_html_node_image(self):
        node = TextNode("This is a text node", text_type_image, "https://www.boot.dev")
        html_node = TextNode.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.children, None)
        self.assertEqual(html_node.props, {"src": "https://www.boot.dev", "alt": "This is a text node"})

if __name__ == "__main__":
    unittest.main()
