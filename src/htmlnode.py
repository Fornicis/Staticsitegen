class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # Constructor method to initialize an HTMLNode instance with optional tag, value, children, and props.
        self.tag = tag  # The HTML tag (e.g., 'div', 'p').
        self.value = value  # The text content or value associated with this node.
        self.children = children  # A list of child nodes.
        self.props = props  # A dictionary of properties/attributes for the node (e.g., {'class': 'my-class'}).

    def to_html(self):
        # Placeholder method to be overridden in subclasses for converting the node to an HTML string.
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        # Method to convert properties dictionary to a string suitable for HTML attributes.
        if self.props is None:  # If there are no properties, return an empty string.
            return ""
        
        # Initialize an empty string to store the HTML attributes.
        props_html = ""
        for prop in self.props:  # Iterate over each property in the dictionary.
            # Format each property as a key="value" string and append it to props_html.
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html  # Return the concatenated string of properties.

    def __repr__(self):
        # Method to provide a string representation of the HTMLNode instance for debugging.
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # Initialize a LeafNode instance with a tag, value, and optional properties.
        # Calls the constructor of the parent class (HTMLNode) with no children.
        super().__init__(tag, value, None, props)

    def to_html(self):
        # Convert the LeafNode to its HTML representation.
        if self.value is None:  # Check if the value is None, which is invalid for HTML.
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:  # If the tag is None, return just the value (plain text).
            return self.value
        # Format the HTML string using the tag, properties, and value.
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        # Provide a string representation of the LeafNode instance for debugging.
        return f"LeafNode({self.tag}, {self.value}, {self.props})"



class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        # Initialize a ParentNode instance with a tag, a list of children nodes, and optional properties.
        # Calls the constructor of the parent class (HTMLNode) with no value.
        super().__init__(tag, None, children, props)

    def to_html(self):
        # Convert the ParentNode and its children to an HTML representation.
        if self.tag is None:  # Ensure the tag is not None, which is invalid for HTML.
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:  # Ensure there are children nodes to process.
            raise ValueError("Invalid HTML: no children")
        
        # Generate HTML for each child node and concatenate them into a single string.
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        
        # Format the HTML string using the tag, properties, and combined children HTML.
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        # Provide a string representation of the ParentNode instance for debugging.
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

