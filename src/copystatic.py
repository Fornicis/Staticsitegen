import os
import shutil

# Function to copy files and directories recursively from source to destination
def copy_files_recursive(source_dir_path, dest_dir_path):
    # Check if the destination directory exists, if not, create it
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    # Iterate through all items in the source directory
    for filename in os.listdir(source_dir_path):
        # Construct full path for source and destination
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        # Check if the item is a file
        if os.path.isfile(from_path):
            # Copy the file to the destination
            shutil.copy(from_path, dest_path)
        else:
            # If the item is a directory, call the function recursively
            copy_files_recursive(from_path, dest_path)
