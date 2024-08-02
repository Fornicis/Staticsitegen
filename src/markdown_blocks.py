block_type_heading = "heading"
block_type_paragraph = "paragraph"
block_type_code = "code"
block_type_olist = "ordered list"
block_type_ulist = "unordered list"
block_type_quote = "quote"

def markdown_to_blocks(markdown):
    # Split the markdown text into blocks based on double newlines.
    blocks = markdown.split("\n\n")
    
    # Initialize an empty list to hold non-empty, stripped blocks.
    filtered_blocks = []
    
    # Iterate over each block obtained from splitting the markdown text.
    for block in blocks:
        # Skip empty blocks resulting from multiple consecutive newlines.
        if block == "":
            continue
        
        # Strip leading and trailing whitespace from the block.
        block = block.strip()
        
        # Append the cleaned block to the list of filtered blocks.
        filtered_blocks.append(block)
    
    # Return the list of filtered, non-empty, and stripped blocks.
    return filtered_blocks

def block_to_block_type(block):
    # Split the block into individual lines based on newline characters.
    lines = block.split("\n")

    # Check if the block is a heading of any level.
    # Markdown headings start with one or more '#' symbols followed by a space.
    if (
        block.startswith("# ")  # H1 heading
        or block.startswith("## ")  # H2 heading
        or block.startswith("### ")  # H3 heading
        or block.startswith("#### ")  # H4 heading
        or block.startswith("##### ")  # H5 heading
        or block.startswith("###### ")  # H6 heading
    ):
        return block_type_heading

    # Check if the block is a code block.
    # Code blocks in Markdown are enclosed in triple backticks (```).
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code

    # Check if the block is a blockquote.
    # Blockquotes in Markdown start with a '>' symbol.
    if block.startswith(">"):
        for line in lines:
            # If any line does not start with '>', it's not a valid blockquote.
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote

    # Check if the block is an unordered list using asterisks.
    # Markdown unordered lists can start with '* '.
    if block.startswith("* "):
        for line in lines:
            # If any line does not start with '* ', it's not a valid unordered list.
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist

    # Check if the block is an unordered list using hyphens.
    # Markdown unordered lists can also start with '- '.
    if block.startswith("- "):
        for line in lines:
            # If any line does not start with '- ', it's not a valid unordered list.
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist

    # Check if the block is an ordered list.
    # Ordered lists in Markdown start with numbers followed by a period and space (e.g., '1. ').
    if block.startswith("1. "):
        i = 1
        for line in lines:
            # If any line does not start with the correct numbering format, it's not a valid ordered list.
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist

    # If none of the conditions are met, the block is considered a paragraph by default.
    return block_type_paragraph