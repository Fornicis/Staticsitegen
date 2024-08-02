import unittest
from markdown_blocks import markdown_to_blocks

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

if __name__ == "__main__":
    # If this script is run directly, execute the test cases.
    unittest.main()