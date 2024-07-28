import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)
#^Imports necessary variables, classes and functions

class TestInlineMarkdown(unittest.TestCase):#Tests to ensure that all split delimeters are in correct position and correct syntax
    def test_delim_bold(self):
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
    def test_single_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        extract_text = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], extract_text)

    def test_double_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extract_text = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), 
                          ("to youtube", "https://www.youtube.com/@bootdotdev")],
                          extract_text)
        
    def test_triple_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and [to runescape](https://www.runescape.com/community)"
        extract_text = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev"),
                          ("to youtube", "https://www.youtube.com/@bootdotdev"),
                          ("to runescape", "https://www.runescape.com/community")],
                          extract_text)
        
    def test_single_image(self):
        image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        extract_image = extract_markdown_images(image)
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif")], extract_image)

    def test_double_image(self):
        image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extract_image = extract_markdown_images(image)
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                        ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")],
                        extract_image)
        
    def test_triple_image(self):
        image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and ![dragon full helm](https://static.wikia.nocookie.net/runescape2/images/a/ae/Dragon_full_helm_detail.png/revision/latest?cb=20120611222412)"
        extract_image = extract_markdown_images(image)
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                        ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
                        ("dragon full helm", "https://static.wikia.nocookie.net/runescape2/images/a/ae/Dragon_full_helm_detail.png/revision/latest?cb=20120611222412")],
                        extract_image)
        
if __name__ == "__main__":
    unittest.main()
