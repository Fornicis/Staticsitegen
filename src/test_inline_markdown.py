import unittest

# Importing functions and classes for handling inline markdown parsing.
from inline_markdown import (
    split_nodes_delimiter,  # Function to split text nodes by a specific delimiter (e.g., ** for bold)
    split_nodes_image,      # Function to process and extract image nodes from text
    split_nodes_link,       # Function to process and extract link nodes from text
    text_to_textnodes,      # Function to convert a text string into a list of text nodes based on markdown syntax
    extract_markdown_images, # Function to extract image information from markdown text
    extract_markdown_links  # Function to extract link information from markdown text
)

# Importing the TextNode class and constants for different text types.
from textnode import (
    TextNode,              # Class representing a text node with a type (e.g., plain text, bold, italic)
    text_type_text,        # Constant representing plain text type
    text_type_bold,        # Constant representing bold text type
    text_type_italic,      # Constant representing italic text type
    text_type_code,        # Constant representing inline code text type
    text_type_link,        # Constant representing hyperlink text type
    text_type_image        # Constant representing image text type
)


class TestInlineMarkdown(unittest.TestCase):
    # Tests for ensuring the correct handling of inline markdown syntax.

    def test_delim_bold(self):
        # Test splitting a single bolded word.
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        # Test splitting two bolded words in one sentence.
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        # Test splitting a bolded phrase and another bolded word.
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        # Test splitting a single italicized word.
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        # Test handling both bold and italic text in one sentence.
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        # Test splitting a code block.
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

class TestInlineMarkdownLinks(unittest.TestCase):
    # Test cases for extracting markdown links from text.

    def test_single_link(self):
        # Test extraction of a single markdown link.
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        extract_text = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], extract_text)

    def test_double_link(self):
        # Test extraction of two markdown links.
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extract_text = extract_markdown_links(text)
        self.assertListEqual([
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ], extract_text)
        
    def test_triple_link(self):
        # Test extraction of three markdown links.
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and [to runescape](https://www.runescape.com/community)"
        extract_text = extract_markdown_links(text)
        self.assertListEqual([
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ("to runescape", "https://www.runescape.com/community")
        ], extract_text)

class TestInlineMarkdownImages(unittest.TestCase):
    # Test cases for extracting markdown images from text.

    def test_single_image(self):
        # Test extraction of a single markdown image.
        image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        extract_image = extract_markdown_images(image)
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif")], extract_image)

    def test_double_image(self):
        # Test extraction of two markdown images.
        image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extract_image = extract_markdown_images(image)
        self.assertListEqual([
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ], extract_image)
        
    def test_triple_image(self):
        # Test extraction of three markdown images.
        image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and ![dragon full helm](https://static.wikia.nocookie.net/runescape2/images/a/ae/Dragon_full_helm_detail.png/revision/latest?cb=20120611222412)"
        extract_image = extract_markdown_images(image)
        self.assertListEqual([
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ("dragon full helm", "https://static.wikia.nocookie.net/runescape2/images/a/ae/Dragon_full_helm_detail.png/revision/latest?cb=20120611222412")
        ], extract_image)

        
class TestInlineMarkdownSplitLinks(unittest.TestCase):
    # Tests the function split_nodes_link to ensure it correctly splits text nodes containing markdown links.

    def test_split_links(self):
        # Test splitting a text node containing two markdown links.
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("another link", text_type_link, "https://blog.boot.dev"),
                TextNode(" with text that follows", text_type_text),
            ],
            new_nodes,
        )

class TestInlineMarkdownSplitImages(unittest.TestCase):
    # Tests the function split_nodes_image to ensure it correctly splits text nodes containing markdown images.

    def test_split_image(self):
        # Test splitting a text node containing a single markdown image.
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        # Test splitting a text node that is solely a markdown image.
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", text_type_image, "https://www.example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        # Test splitting a text node containing two markdown images.
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


class TestInlineMarkdownTextToTextNodes(unittest.TestCase):
    # Tests the text_to_textnodes function, which converts a markdown-formatted string into a list of TextNode objects.

    def test_text_to_textnodes(self):
        # Test the conversion of a markdown string into TextNode objects, ensuring all elements are correctly identified and categorized.
        nodes = text_to_textnodes(
            "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),  # Plain text node
                TextNode("text", text_type_bold),  # Bold text node
                TextNode(" with an ", text_type_text),  # Plain text node
                TextNode("italic", text_type_italic),  # Italic text node
                TextNode(" word and a ", text_type_text),  # Plain text node
                TextNode("code block", text_type_code),  # Code block node
                TextNode(" and an ", text_type_text),  # Plain text node
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),  # Image node
                TextNode(" and a ", text_type_text),  # Plain text node
                TextNode("link", text_type_link, "https://boot.dev"),  # Link node
            ],
            nodes,
        )


if __name__ == "__main__":
    unittest.main()
