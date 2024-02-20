#! python3
# zipFileCompress.py - Compresses folder in directory tree with largest disk space
# into a ZIP file to save storage

import os
import shutil

def find_largest_folder_by_size(starting_path):
    max_folder = ''
    max_size = 0

    for foldername, subfolders, filenames in os.walk(starting_path):
        folder_size = sum(os.path.getsize(os.path.join(foldername, filename)) for filename in filenames)

        if folder_size > max_size:
            max_folder = foldername
            max_size = folder_size

    return max_folder, max_size

def compress_folder(folder_path, archive_name):
    shutil.make_archive(archive_name, 'zip', folder_path)    # create a zip archive of the specified folder.

# Provide the starting path for the directory tree
starting_path = '/path/to/your/directory'

largest_folder, folder_size = find_largest_folder_by_size(starting_path)

print(f"The folder using the most disk space is '{largest_folder}' with a size of {folder_size} bytes.")

# Compress the largest folder
archive_name = 'compressed_folder'
compress_folder(largest_folder, archive_name)

print(f"The contents of '{largest_folder}' have been compressed to '{archive_name}.zip'.")
