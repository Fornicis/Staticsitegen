from textnode import (#Imports necessary classes and variables
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)
import re

def text_to_textnodes(text):
    # Function to convert a given text into a list of TextNode objects, processing various Markdown formatting and media types.

    # Initialize the list of nodes with a single TextNode containing the entire input text.
    nodes = [TextNode(text, text_type_text)]
    
    # Process bold text by splitting the nodes on the '**' delimiter and tagging bold text.
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    
    # Process italic text by splitting the nodes on the '*' delimiter and tagging italic text.
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    
    # Process inline code by splitting the nodes on the '`' delimiter and tagging code text.
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    
    # Process image nodes by splitting and creating separate nodes for image references.
    nodes = split_nodes_image(nodes)
    
    # Process link nodes by splitting and creating separate nodes for link references.
    nodes = split_nodes_link(nodes)
    
    # Return the list of processed TextNode objects.
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # Function to split nodes by their delimiter and categorize text types.

    new_nodes = []  # Create an empty list to store the result nodes after processing.

    for old_node in old_nodes:  # Iterate through each node in the old_nodes list.
        # Check if the node's text_type does not match the expected text_type.
        if old_node.text_type != text_type:
            new_nodes.append(old_node)  # If text_type doesn't match, add the node to new_nodes as is.
            continue

        split_nodes = []  # Create an empty list to store nodes that result from splitting.

        # Split the node's text content by the given delimiter.
        sections = old_node.text.split(delimiter)

        # Check if the number of sections is even; this indicates a syntax error (unclosed formatted section).
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")

        # Iterate through the split sections to create new nodes based on their positions.
        for i in range(len(sections)):
            # Skip empty sections.
            if sections[i] == "":
                continue
            
            # Create a new TextNode for each non-empty section.
            # Alternate between text_type and the given text_type based on the section's index.
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        # Extend the new_nodes list with the newly created split nodes.
        new_nodes.extend(split_nodes)

    return new_nodes  # Return the list of new nodes after processing all old nodes.


def extract_markdown_images(text):
    # Function to extract Markdown image references from a text.
    pattern = r"!\[(.*?)\]\((.*?)\)"
    # Regular expression pattern to match Markdown image syntax:
    # ![alt text](URL)
    # (.*?) captures the alt text and URL as separate groups.
    matches = re.findall(pattern, text)
    # Find all matches of the pattern in the given text.
    return matches
    # Return a list of tuples, each containing the alt text and URL of an image.

def extract_markdown_links(text):
    # Function to extract Markdown link references from a text.
    pattern = r"\[(.*?)\]\((.*?)\)"
    # Regular expression pattern to match Markdown link syntax:
    # [link text](URL)
    # (.*?) captures the link text and URL as separate groups.
    matches = re.findall(pattern, text)
    # Find all matches of the pattern in the given text.
    return matches
    # Return a list of tuples, each containing the link text and URL of a link.

def split_nodes_image(old_nodes):
    # Function to process a list of nodes, splitting nodes that contain Markdown images into separate nodes.

    new_nodes = []  # Create an empty list to store the result nodes after processing.

    for old_node in old_nodes:  # Iterate through each node in the old_nodes list.
        # Check if the node's text_type does not match text_type_text.
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)  # If text_type doesn't match, add the node to new_nodes as is.
            continue
        
        original_text = old_node.text  # Get the text content of the current node.
        images = extract_markdown_images(original_text)  # Extract Markdown images from the text.

        # If no images are found, add the node to new_nodes without modification.
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        
        # Process each extracted image.
        for image in images:
            # Split the text at the Markdown image syntax.
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)

            # Check if the split resulted in exactly two sections (before and after the image).
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")

            # If there is text before the image, create a TextNode for it.
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            
            # Create a TextNode for the image, including alt text, text_type_image, and URL.
            new_nodes.append(
                TextNode(
                    image[0],  # Alt text for the image.
                    text_type_image,  # Text type indicating this is an image.
                    image[1]  # URL of the image.
                )
            )
            
            # Update original_text to the text after the image.
            original_text = sections[1]
        
        # If there is remaining text after the last image, create a TextNode for it.
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    
    return new_nodes  # Return the list of new nodes after processing.


def split_nodes_link(old_nodes):
    # Function to process a list of nodes, splitting nodes that contain Markdown links into separate nodes.

    new_nodes = []  # Create an empty list to store the result nodes after processing.

    for old_node in old_nodes:  # Iterate through each node in the old_nodes list.
        # Check if the node's text_type does not match text_type_text.
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)  # If text_type doesn't match, add the node to new_nodes as is.
            continue
        
        original_text = old_node.text  # Get the text content of the current node.
        links = extract_markdown_links(original_text)  # Extract Markdown links from the text.

        # If no links are found, add the node to new_nodes without modification.
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        
        # Process each extracted link.
        for link in links:
            # Split the text at the Markdown link syntax.
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)

            # Check if the split resulted in exactly two sections (before and after the link).
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")

            # If there is text before the link, create a TextNode for it.
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            
            # Create a TextNode for the link, including link text, text_type_link, and URL.
            new_nodes.append(
                TextNode(
                    link[0],  # Link text.
                    text_type_link,  # Text type indicating this is a link.
                    link[1]  # URL of the link.
                )
            )
            
            # Update original_text to the text after the link.
            original_text = sections[1]
        
        # If there is remaining text after the last link, create a TextNode for it.
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    
    return new_nodes  # Return the list of new nodes after processing.



