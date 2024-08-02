from htmlnode import LeafNode  # Imports the LeafNode class from the htmlnode module

# Defines constants for different types of markdown syntax
text_type_text = "text"       # Represents plain text without any formatting
text_type_bold = "bold"       # Represents text formatted as bold
text_type_italic = "italic"   # Represents text formatted as italic
text_type_code = "code"       # Represents inline code text
text_type_link = "link"       # Represents hyperlinks
text_type_image = "image"     # Represents image references


class TextNode:
    # Class to represent a segment of text with associated Markdown syntax and optional URL.

    def __init__(self, text, text_type, url=None):
        # Initialize a TextNode instance with text, text type, and an optional URL.
        self.text = text  # The content of the text node.
        self.text_type = text_type  # The type of formatting or media (e.g., bold, italic, link).
        self.url = url  # Optional URL, used for links and images.

    def __eq__(self, other):
        # Equality check for TextNode instances. Two nodes are considered equal if their text, text_type, and URL are identical.
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        # String representation of the TextNode instance, useful for debugging and logging.
        return f"TextNode({self.text}, {self.text_type}, {self.url})"



def text_node_to_html_node(text_node):
    # Converts a TextNode instance into an HTML node (LeafNode) based on its type.

    if text_node.text_type == text_type_text:
        # If the text type is plain text, create a LeafNode with no HTML tag.
        return LeafNode(None, text_node.text)
    
    if text_node.text_type == text_type_bold:
        # If the text type is bold, create a LeafNode with the <b> tag.
        return LeafNode("b", text_node.text)
    
    if text_node.text_type == text_type_italic:
        # If the text type is italic, create a LeafNode with the <i> tag.
        return LeafNode("i", text_node.text)
    
    if text_node.text_type == text_type_code:
        # If the text type is code, create a LeafNode with the <code> tag.
        return LeafNode("code", text_node.text)
    
    if text_node.text_type == text_type_link:
        # If the text type is a link, create a LeafNode with the <a> tag and include the href attribute.
        return LeafNode("a", text_node.text, {"href": text_node.url})
    
    if text_node.text_type == text_type_image:
        # If the text type is an image, create a LeafNode with the <img> tag and include src and alt attributes.
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    
    # Raise an error if the text type is not recognized.
    raise ValueError(f"Invalid text type: {text_node.text_type}")

