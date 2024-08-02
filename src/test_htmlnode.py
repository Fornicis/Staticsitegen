import unittest
from htmlnode import LeafNode, ParentNode, HTMLNode#Imports all necessary classes and modules


import unittest
from htmlnode import LeafNode, ParentNode, HTMLNode  # Imports all necessary classes and modules

class TestHTMLNode(unittest.TestCase):
    # Test suite for validating the functionality of the HTMLNode class and its methods.

    def test_to_html_props(self):
        # Tests the props_to_html method of the HTMLNode class.
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
        # Asserts that the props_to_html method generates the correct HTML attributes for the node.

    def test_values(self):
        # Tests the basic attributes of the HTMLNode class.
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        # Asserts that the tag attribute is set correctly.

        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        # Asserts that the value attribute is set correctly.

        self.assertEqual(
            node.children,
            None,
        )
        # Asserts that the children attribute is set to None by default.

        self.assertEqual(
            node.props,
            None,
        )
        # Asserts that the props attribute is set to None by default.


    def test_repr(self):
    # Test for the __repr__ method of the HTMLNode class to ensure it produces the correct string representation.
    
        node = HTMLNode(
            "p",                             # Tag name of the HTML node.
            "What a strange world",          # Text content of the HTML node.
            None,                            # Children of the HTML node (none in this case).
            {"class": "primary"},            # Properties of the HTML node (attributes).
        )
        
        self.assertEqual(
            node.__repr__(),                 # Calls the __repr__ method on the HTMLNode instance.
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",  # Expected string representation of the HTMLNode instance.
        )
    # Asserts that the actual output of __repr__ matches the expected output.


    def test_to_html_no_children(self):
    # Test case for LeafNode to_html method when there are no children nodes.
    # Checks if a simple HTML element with text content is correctly formatted.
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        # Test case for LeafNode to_html method when there is no tag.
        # Checks if the text content is returned as-is without HTML tags.
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        # Test case for ParentNode to_html method with one child node.
        # Checks if a parent node correctly wraps a single child node in HTML.
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        # Test case for ParentNode to_html method with nested children (grandchildren).
        # Checks if nested structures are correctly represented in HTML output.
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        # Test case for ParentNode to_html method with multiple children of different types.
        # Ensures that the parent node correctly concatenates different child nodes in HTML output.
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),   # Bold text
                LeafNode(None, "Normal text"), # Normal text
                LeafNode("i", "italic text"), # Italic text
                LeafNode(None, "Normal text"), # Normal text
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        # Test case for ParentNode to_html method with heading tags.
        # Checks if the heading structure with multiple children is correctly represented in HTML.
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),   # Bold text
                LeafNode(None, "Normal text"), # Normal text
                LeafNode("i", "italic text"), # Italic text
                LeafNode(None, "Normal text"), # Normal text
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )



if __name__ == "__main__":
    unittest.main()
