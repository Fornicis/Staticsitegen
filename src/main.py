import os
import shutil
from copystatic import copy_files_recursive

# Define paths for source (static) and destination (public) directories
dir_path_static = "./static"
dir_path_public = "./public"

# Main function to manage the process of cleaning and copying files
def main():
    # Print a message indicating the start of the deletion process
    print("Deleting public directory...")
    # Check if the public directory exists
    if os.path.exists(dir_path_public):
        # Remove the public directory and all its contents
        shutil.rmtree(dir_path_public)

    # Print a message indicating the start of the copying process
    print("Copying static files to public directory...")
    # Call the copy_files_recursive function to copy all files and directories
    # from the static directory to the public directory
    copy_files_recursive(dir_path_static, dir_path_public)

# Entry point of the script
main()
