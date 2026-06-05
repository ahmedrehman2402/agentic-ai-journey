import os
import shutil

def organize_files():
    # Ask the user which folder they want to organize
    folder_path = input("Enter the path of the folder to organize (or press Enter for current folder): ")
    
    # If they just press Enter, use the folder the script is currently in
    if folder_path == "":
        folder_path = os.getcwd()
        
    # Check if the folder actually exists
    if not os.path.exists(folder_path):
        print("That folder does not exist!")
        return

    print(f"Organizing files in: {folder_path}")

    # A simple dictionary to map file extensions to folder names
    extensions_map = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.csv'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz']
    }

    # Go through every item in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip if it's already a folder (we only want to organize files)
        if os.path.isdir(file_path):
            continue
            
        # Skip the script itself so it doesn't move itself
        if filename == "week-01-file-organizer.py":
            continue

        # Get the file extension (like .txt)
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # Figure out which folder it belongs to
        moved = False
        for folder_name, extensions_list in extensions_map.items():
            if file_extension in extensions_list:
                # Create the category folder if it doesn't exist yet
                target_folder = os.path.join(folder_path, folder_name)
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                
                # Move the file
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved: {filename} -> {folder_name}/")
                moved = True
                break
                
        # Put anything unrecognized in an "Others" folder
        if not moved and file_extension != '':
            other_folder = os.path.join(folder_path, "Others")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved: {filename} -> Others/")

    print("Finished organizing files!")

if __name__ == "__main__":
    organize_files()
