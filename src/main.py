import os
import shutil

from copystatic import copy_files_recursive  # Import function to copy static files
from gencontent import generate_pages_recursive  # Import function to generate pages from content


dir_path_static = "./static"  # Path to static files directory
dir_path_public = "./public"  # Path to public output directory
dir_path_content = "./content"  # Path to content files directory
template_path = "./template.html"  # Path to HTML template file


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):  # Check if the public directory exists
        shutil.rmtree(dir_path_public)  # Remove the public directory and its contents

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)  # Copy static files to the public directory

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)  # Generate HTML pages from content


main()  # Call the main function to execute the script
