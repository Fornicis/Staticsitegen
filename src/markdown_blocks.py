from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

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

def markdown_to_html_node(markdown):
    # Convert the markdown text into blocks.
    blocks = markdown_to_blocks(markdown)
    
    # Initialize an empty list to hold the HTML nodes.
    children = []
    
    # Iterate over each block, convert it to an HTML node, and append to the children list.
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    
    # Return a parent HTML node of type "div" containing all the children.
    return ParentNode("div", children, None)



def block_to_html_node(block):
    # Determine the type of the block.
    block_type = block_to_block_type(block)
    
    # Convert the block to the corresponding HTML node type.
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    
    # Raise an error if the block type is unrecognized.
    raise ValueError("Invalid block type")



def text_to_children(text):
    # Convert the text into a list of text nodes.
    text_nodes = text_to_textnodes(text)
    
    # Initialize an empty list to hold the HTML nodes.
    children = []
    
    # Convert each text node into an HTML node and append to the children list.
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    
    # Return the list of HTML nodes.
    return children



def paragraph_to_html_node(block):
    # Split the block into lines and join them into a single string.
    lines = block.split("\n")
    paragraph = " ".join(lines)
    
    # Convert the paragraph text into HTML nodes.
    children = text_to_children(paragraph)
    
    # Return a parent HTML node of type "p" containing the children.
    return ParentNode("p", children)



def heading_to_html_node(block):
    # Determine the heading level based on the number of leading "#" characters.
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    
    # Validate the heading level and block length.
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    
    # Extract the heading text.
    text = block[level + 1 :]
    
    # Convert the heading text into HTML nodes.
    children = text_to_children(text)
    
    # Return a parent HTML node of the appropriate heading level (e.g., <h1>, <h2>).
    return ParentNode(f"h{level}", children)



def code_to_html_node(block):
    # Validate the code block format.
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    
    # Extract the code text, excluding the triple backticks.
    text = block[4:-3]
    
    # Convert the code text into HTML nodes.
    children = text_to_children(text)
    
    # Wrap the code in a <code> element, then wrap in a <pre> element.
    code = ParentNode("code", children)
    return ParentNode("pre", [code])



def olist_to_html_node(block):
    # Split the block into list items.
    items = block.split("\n")
    
    # Initialize an empty list to hold the list item HTML nodes.
    html_items = []
    
    # Process each list item.
    for item in items:
        # Extract the text after the "1. " prefix (or similar numbering).
        text = item[3:]
        
        # Convert the list item text into HTML nodes.
        children = text_to_children(text)
        
        # Create an <li> element for each item and add to the list.
        html_items.append(ParentNode("li", children))
    
    # Return a parent HTML node of type "ol" containing the list items.
    return ParentNode("ol", html_items)



def ulist_to_html_node(block):
    # Split the block into list items.
    items = block.split("\n")
    
    # Initialize an empty list to hold the list item HTML nodes.
    html_items = []
    
    # Process each list item.
    for item in items:
        # Extract the text after the "* " or "- " prefix.
        text = item[2:]
        
        # Convert the list item text into HTML nodes.
        children = text_to_children(text)
        
        # Create an <li> element for each item and add to the list.
        html_items.append(ParentNode("li", children))
    
    # Return a parent HTML node of type "ul" containing the list items.
    return ParentNode("ul", html_items)



def quote_to_html_node(block):
    # Split the block into lines.
    lines = block.split("\n")
    
    # Initialize an empty list to hold the cleaned quote lines.
    new_lines = []
    
    # Process each line in the quote block.
    for line in lines:
        # Ensure each line starts with a ">".
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        
        # Remove the ">" and strip any leading/trailing whitespace.
        new_lines.append(line.lstrip(">").strip())
    
    # Join the cleaned lines into a single string.
    content = " ".join(new_lines)
    
    # Convert the quote content into HTML nodes.
    children = text_to_children(content)
    
    # Return a parent HTML node of type "blockquote" containing the children.
    return ParentNode("blockquote", children)
