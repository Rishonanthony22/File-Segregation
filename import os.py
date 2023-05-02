import os
import shutil

from_dir = "/path/to/Downloads"
to_dir = "/path/to/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    # Skip files with no extension
    if not extension:
        continue
    
    # Move files with certain extensions
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files", extension[1:].upper() + "_Files")
        path3 = os.path.join(path2, file_name)
        
        # Check if directory exists, otherwise create it
        if not os.path.exists(path2):
            os.makedirs(path2)
            print(f"Created directory {path2}")
        
        # Move the file to the destination directory
        shutil.move(path1, path3)
        print(f"Moved {file_name} to {path3}")
