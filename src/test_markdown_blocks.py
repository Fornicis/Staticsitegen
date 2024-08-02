import unittest
from markdown_blocks import (
    markdown_to_html_node,
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_code,
    block_type_heading,
    block_type_olist,
    block_type_quote,
    block_type_ulist
)

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        # Test the function with standard markdown input containing paragraphs, bold, italic, and code formatting.
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        # Call the markdown_to_blocks function and store the result in the 'blocks' variable.
        blocks = markdown_to_blocks(md)

        # Check if the returned list of blocks matches the expected list.
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        # Test the function with markdown input containing extra newlines between paragraphs.
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        # Call the markdown_to_blocks function and store the result in the 'blocks' variable.
        blocks = markdown_to_blocks(md)

        # Check if the returned list of blocks correctly ignores extra newlines and matches the expected output.
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
class TestBlockToBlock(unittest.TestCase):
    def test_block_to_block_types(self):
        # Test if the function correctly identifies a heading block.
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)

        # Test if the function correctly identifies a code block.
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)

        # Test if the function correctly identifies a quote block.
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)

        # Test if the function correctly identifies an unordered list block using asterisks.
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)

        # Test if the function correctly identifies an ordered list block.
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)

        # Test if the function correctly identifies a paragraph block.
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

class TestMarkdownToHtml(unittest.TestCase):
    # Test case for a single paragraph with bolded text.
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""
        # Convert markdown to HTML node tree.
        node = markdown_to_html_node(md)
        # Convert the HTML node tree to HTML string.
        html = node.to_html()
        # Assert the HTML output matches the expected value.
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    # Test case for multiple paragraphs with mixed formatting.
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""
        # Convert markdown to HTML node tree.
        node = markdown_to_html_node(md)
        # Convert the HTML node tree to HTML string.
        html = node.to_html()
        # Assert the HTML output matches the expected value.
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    # Test case for unordered and ordered lists.
    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""
        # Convert markdown to HTML node tree.
        node = markdown_to_html_node(md)
        # Convert the HTML node tree to HTML string.
        html = node.to_html()
        # Assert the HTML output matches the expected value.
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    # Test case for headings and paragraph text.
    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""
        # Convert markdown to HTML node tree.
        node = markdown_to_html_node(md)
        # Convert the HTML node tree to HTML string.
        html = node.to_html()
        # Assert the HTML output matches the expected value.
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    # Test case for blockquote and paragraph text.
    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""
        # Convert markdown to HTML node tree.
        node = markdown_to_html_node(md)
        # Convert the HTML node tree to HTML string.
        html = node.to_html()
        # Assert the HTML output matches the expected value.
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    # Test case for blockquote and paragraph text (duplicate test, can be removed).
    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""
        # Convert markdown to HTML node tree.
        node = markdown_to_html_node(md)
        # Convert the HTML node tree to HTML string.
        html = node.to_html()
        # Assert the HTML output matches the expected value.
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    # If this script is run directly, execute the test cases.
    unittest.main()