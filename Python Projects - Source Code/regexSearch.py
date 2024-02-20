# A program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression

import os
import re

def search_files(folder_path, regex_pattern):
    # Validate folder path
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid folder path.")
        return

    # Compile the regular expression pattern
    pattern = re.compile(regex_pattern)

    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)

            # Open and read the file
            with open(file_path, 'r') as file:
                # Search for lines matching the regex pattern
                for line_number, line in enumerate(file, start=1):
                    if pattern.search(line):
                        print(f"{filename}: Line {line_number}: {line.strip()}")

# Example usage
folder_to_search = '/path/to/your/folder'
user_regex_pattern = input("Enter a regular expression pattern: ")

search_files(folder_to_search, user_regex_pattern)
