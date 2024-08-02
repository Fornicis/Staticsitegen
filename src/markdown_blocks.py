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