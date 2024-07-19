import unittest
from htmlnode import LeafNode, ParentNode, HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple(self):
        node = HTMLNode(tag="a", value="Link", children=[], props={"href": "https://www.google.co.uk", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.co.uk" target="_blank"')

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p", value="text", children=[], props={})
        self.assertEqual(node.props_to_html(), '')
    
    def test_props_to_html_single(self):
        node = HTMLNode(tag="img", value="", children=[], props= {"src": "image.png"})
        self.assertEqual(node.props_to_html(), 'src="image.png"')

    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="span", value="some random text")
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_special(self):
        node = HTMLNode(tag="input", value="", children=[], props={"type": "text", "placeholder": "Enter your name"})
        self.assertEqual(node.props_to_html(), 'type="text" placeholder="Enter your name"')
    
    def test_repr(self):
        node = HTMLNode("p", "What a strange world", None, {"class": "primary"})
        self.assertEqual(node.__repr__(), "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})")

    def test_to_html_props(self):
        node = HTMLNode("div", "Hello world!", None, {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(node.props_to_html(), 'class="greeting" href="https://boot.dev"')

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tage(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>",)


    def test_to_html_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold Text"),
                LeafNode(None, "Normal Text"),
                LeafNode("i", "Italic Text"),
                LeafNode(None, "Normal Text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold Text</b>Normal Text<i>Italic Text</i>Normal Text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold Text"),
                LeafNode(None, "Normal Text"),
                LeafNode("i", "Italic Text"),
                LeafNode(None, "Normal Text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold Text</b>Normal Text<i>Italic Text</i>Normal Text</h2>",
        )
if __name__ == "__main__":
    unittest.main()