import unittest
from gencontent import extract_title

# Test case class for testing the extract_title function
class TestExtractTitle(unittest.TestCase):

    # Test case for extracting a simple title
    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    # Test case for a markdown string with multiple titles, expecting only the first to be extracted
    def test_eq_double(self):
        actual = extract_title(
            """
# This is a title

# This is a second title that should be ignored
"""
        )
        self.assertEqual(actual, "This is a title")

    # Test case for a title with additional content following it
    def test_eq_long(self):
        actual = extract_title(
            """
# title

this is a bunch

of text

* and
* a
* list
"""
        )
        self.assertEqual(actual, "title")

    # Test case for content without a title, expecting an exception
    def test_none(self):
        try:
            extract_title(
                """
no title
"""
            )
            self.fail("Should have raised an exception")
        except Exception as e:
            pass

# Main block to execute the test cases
if __name__ == "__main__":
    unittest.main()
