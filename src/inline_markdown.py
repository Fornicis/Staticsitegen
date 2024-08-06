import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

# Function to convert plain text into a list of TextNode objects with various text types
def text_to_textnodes(text):
    # Start with the entire text as a single text node
    nodes = [TextNode(text, text_type_text)]
    # Split text nodes into bold nodes where "**" delimiter is found
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    # Split text nodes into italic nodes where "*" delimiter is found
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    # Split text nodes into code nodes where "`" delimiter is found
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    # Split text nodes into image nodes
    nodes = split_nodes_image(nodes)
    # Split text nodes into link nodes
    nodes = split_nodes_link(nodes)
    # Return the list of text nodes
    return nodes

# Function to split text nodes based on a delimiter and create nodes of a specified type
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        # If the node is not a plain text node, add it to new_nodes without changes
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        # Split the text by the delimiter
        sections = old_node.text.split(delimiter)
        # Check for unbalanced delimiter sections
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        # Iterate over sections to create text nodes
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            # Even-indexed sections are plain text, odd-indexed are the specified text type
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

# Function to identify and convert image markdown syntax into image text nodes
def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        # If the node is not a plain text node, add it to new_nodes without changes
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        # Extract all image syntax from the text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        # Iterate over found images and replace them with image text nodes
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

# Function to identify and convert link markdown syntax into link text nodes
def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        # If the node is not a plain text node, add it to new_nodes without changes
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        # Extract all link syntax from the text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        # Iterate over found links and replace them with link text nodes
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

# Function to extract all image markdown syntax from text
def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

# Function to extract all link markdown syntax from text
def extract_markdown_links(text):
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches
