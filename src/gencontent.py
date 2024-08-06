import os
from markdown_blocks import markdown_to_html_node

# Function to generate an HTML page from a markdown file and a template
def generate_page(from_path, template_path, dest_path):
    # Log the paths being processed
    print(f" * {from_path} {template_path} -> {dest_path}")

    # Open and read the markdown file
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    # Open and read the template file
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    # Convert the markdown content to an HTML node
    node = markdown_to_html_node(markdown_content)
    # Convert the HTML node to a string of HTML
    html = node.to_html()

    # Extract the title from the markdown content
    title = extract_title(markdown_content)
    # Replace placeholders in the template with the actual title and content
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    # Ensure the destination directory exists
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    
    # Write the final HTML to the destination file
    to_file = open(dest_path, "w")
    to_file.write(template)

# Function to extract the title from the markdown content
def extract_title(md):
    # Split the markdown content into lines
    lines = md.split("\n")
    # Iterate over the lines to find the title
    for line in lines:
        # Check if the line starts with a level 1 heading indicator ("# ")
        if line.startswith("# "):
            # Return the title, which follows the "# "
            return line[2:]
    # Raise an error if no title is found
    raise ValueError("No title found")
