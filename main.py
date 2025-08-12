import os # --> for file and directory operations
import sys # --> for file operations

def organize_files(folder_path, simulate=False):
    """
    Organizes files in the specified folder into subfolders based on file type.
    
    Parameters:
    folder_path (str): The path to the folder containing files to organize.
    simulate (bool): If True, only simulates the organization without making changes.
    """

    # Step(2) Scan for files only
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if not os.path.isfile(file_path):
            continue
        print(f"Found file: {filename}")

def main():
    # Step(1) Accept folder path
    if len(sys.argv) < 2:
        folder_path = input("Enter folder path: ").strip()
    else:
        folder_path = sys.argv[1]

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return
        
    print(f"Processing folder: {folder_path}")

    organize_files(folder_path)

# Running the script
if __name__ == "__main__":
    main()