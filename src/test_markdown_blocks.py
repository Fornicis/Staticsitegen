import unittest
from markdown_blocks import (
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


if __name__ == "__main__":
    # If this script is run directly, execute the test cases.
    unittest.main()