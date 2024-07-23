from textnode import (#Imports necessary classes and variables
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):#Function splits nodes by their delimiter
    new_nodes = []#Creates empty list for result
    for old_node in old_nodes:#Checks to see if the given node is of expected type, if not appends node to result
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []#Creates empty list for nodes that are split
        sections = old_node.text.split(delimiter)#Sets sections variable to the node parts split by delimeter
        if len(sections) % 2 == 0:#Checks to make sure format syntax are closed
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):#Checks and appends any part of the given node which match criteria
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
