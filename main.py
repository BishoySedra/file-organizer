import os # --> for file and directory operations
import sys # --> for file operations
import shutil # --> for file operations

# Step(3) Define file categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
}

def organize_files(folder_path, simulate=False):
    """
    Organizes files in the specified folder into subfolders based on file type.
    
    Parameters:
    folder_path (str): The path to the folder containing files to organize.
    simulate (bool): If True, only simulates the organization without making changes.
    """
    # Step(5.1) Summary counter
    summary = { category: 0 for category in CATEGORIES.keys() }
    summary["Others"] = 0

    # Step(2) Scan for files only
    for filename in os.listdir(folder_path):

        file_path = os.path.join(folder_path, filename)
        if not os.path.isfile(file_path):
            continue
        print(f"Found file: {filename}")

        extension = os.path.splitext(filename)[1].lower()
        category = next((cat for cat, exts in CATEGORIES.items() if extension in exts), "Others")

        target_dir = os.path.join(folder_path, category)

        if not simulate:
            os.makedirs(target_dir, exist_ok=True)
            # Step(4) Move files to their respective directories
            shutil.move(file_path, os.path.join(target_dir, filename))

        summary[category] += 1

    # Step(5.2) Print summary
    print("\nSummary of organized files:")
    for category, count in summary.items():
        print(f"{category}: {count} files")


def main():
    # Step(1) Accept folder path
    if len(sys.argv) < 2:
        folder_path = input("Enter folder path: ").strip()
    else:
        folder_path = sys.argv[1]

    simulate = "--simulate" in sys.argv

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return
        
    print(f"Processing folder: {folder_path}")

    organize_files(folder_path, simulate)

# Running the script
if __name__ == "__main__":
    main()