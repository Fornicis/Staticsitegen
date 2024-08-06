class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # Initialize the HTMLNode with optional attributes: tag, value, children, and props
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        # Method to convert the node to an HTML string, must be implemented in subclasses
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        # Convert the properties dictionary to a string of HTML attributes
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        # Return a string representation of the HTMLNode
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # Initialize the LeafNode, calling the parent constructor
        super().__init__(tag, value, None, props)

    def to_html(self):
        # Convert the LeafNode to an HTML string
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        # Return a string representation of the LeafNode
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        # Initialize the ParentNode, calling the parent constructor
        super().__init__(tag, None, children, props)

    def to_html(self):
        # Convert the ParentNode and its children to an HTML string
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        # Return a string representation of the ParentNode
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
