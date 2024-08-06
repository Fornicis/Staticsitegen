from htmlnode import LeafNode

# Constants representing different text types
text_type_text = "text"        # Plain text
text_type_bold = "bold"        # Bold text
text_type_italic = "italic"    # Italic text
text_type_code = "code"        # Code text
text_type_link = "link"        # Link text
text_type_image = "image"      # Image text

# Class representing a text node with associated metadata
class TextNode:
    def __init__(self, text, text_type, url=None):
        # Initialize a TextNode with text, text type, and optional URL
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        # Compare two TextNode instances for equality based on text, text type, and URL
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        # Provide a string representation of the TextNode instance
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

# Function to convert a TextNode to an HTML node
def text_node_to_html_node(text_node):
    # Convert text node to corresponding HTML node based on text type
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)  # Plain text
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)   # Bold text
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)   # Italic text
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)  # Code text
    if text_node.text_type == text_type_link:
        # Link text with an href attribute
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        # Image text with src and alt attributes
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    # Raise an error if the text type is invalid
    raise ValueError(f"Invalid text type: {text_node.text_type}")
