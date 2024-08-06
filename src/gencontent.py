import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

# Function to recursively generate HTML pages from markdown content
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Iterate over each item in the content directory
    for filename in os.listdir(dir_path_content):
        # Construct the full source and destination paths
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        # Check if the current item is a file
        if os.path.isfile(from_path):
            # Change the extension of the destination file to .html
            dest_path = Path(dest_path).with_suffix(".html")
            # Generate the HTML page
            generate_page(from_path, template_path, dest_path)
        else:
            # If the item is a directory, call this function recursively
            generate_pages_recursive(from_path, template_path, dest_path)

# Function to generate an HTML page from a markdown file and a template
def generate_page(from_path, template_path, dest_path):
    # Log the file paths being processed
    print(f" * {from_path} {template_path} -> {dest_path}")
    # Open and read the markdown file
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    # Open and read the template file
    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    # Convert markdown content to an HTML node
    node = markdown_to_html_node(markdown_content)
    # Convert the HTML node to HTML string
    html = node.to_html()

    # Extract the title from the markdown content
    title = extract_title(markdown_content)
    # Replace the placeholders in the template with the title and content
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    # Ensure the destination directory exists
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    # Write the rendered HTML to the destination file
    to_file = open(dest_path, "w")
    to_file.write(template)

# Function to extract the title from markdown content
def extract_title(md):
    # Split the markdown content into lines
    lines = md.split("\n")
    # Iterate over the lines to find the first level 1 heading
    for line in lines:
        if line.startswith("# "):
            # Return the text after "# " as the title
            return line[2:]
    # Raise an error if no title is found
    raise ValueError("No title found")
