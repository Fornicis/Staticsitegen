import os
import shutil

# Function to recursively copy files and directories from source to destination
def copy_files_recursive(source_dir_path, dest_dir_path):
    # Check if the destination directory exists, if not, create it
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    # Iterate through all items in the source directory
    for filename in os.listdir(source_dir_path):
        # Construct full path to source and destination
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        
        # Print the source and destination paths
        print(f" * {from_path} -> {dest_path}")
        
        # Check if the current item is a file
        if os.path.isfile(from_path):
            # Copy the file to the destination directory
            shutil.copy(from_path, dest_path)
        else:
            # If the current item is a directory, call the function recursively
            copy_files_recursive(from_path, dest_path)
