#! python3
# fileMgmt.py - Searches for files < 100MB and gives option to
# send2trash or compress file to save storage

import os
import send2trash
import shutil

def find_large_files(starting_path, size_threshold):
    large_files = []
    for foldername, subfolders, filenames in os.walk(starting_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            file_size = os.path.getsize(file_path)
            # Check if the file size exceeds the threshold
            if file_size > size_threshold:
                large_files.append(file_path)
    return large_files

def delete_file(file_path):
    try:
        send2trash.send2trash(file_path)
        print(f"File '{file_path}' sent to trash.")
    except Exception as e:
        print(f"Error deleting file '{file_path}': {e}")

def compress_file(file_path):
    try:
        shutil.make_archive(file_path, 'zip', os.path.dirname(file_path), os.path.basename(file_path))
        print(f"File '{file_path}' compressed successfully.")
    except Exception as e:
        print(f"Error compressing file '{file_path}': {e}")

def main():
    starting_path = input("Enter the root of the directory tree you want to search: ")
    size_threshold = 100 * 1024 * 1024  # 100MB

    if not os.path.exists(starting_path):
        print("Invalid path. Exiting.")
        return

    large_files = find_large_files(starting_path, size_threshold)

    print("Large files found:")
    for i, file_path in enumerate(large_files, 1):
        print(f"{i}. {file_path}")

    if large_files:
        choice = input("Enter the number of the file you want to process (or 'q' to quit): ")
        if choice.lower() != 'q' and choice.isdigit() and 0 < int(choice) <= len(large_files):
            selected_file = large_files[int(choice) - 1]
            action = input(f"Do you want to delete or compress '{selected_file}'? Enter 'd' for delete, 'c' for compress: ")
            if action.lower() == 'd':
                delete_file(selected_file)
            elif action.lower() == 'c':
                compress_file(selected_file)
            else:
                print("Invalid choice. Exiting.")
        else:
            print("Exiting.")
    else:
        print("No large files found.")

if __name__ == "__main__":
    main()
