import os  # For file and directory operations
import sys  # For handling command-line arguments
import shutil  # For moving files between directories

# Step(3) Define file categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],  # Common image file extensions
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],  # Document file extensions
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],  # Video file extensions
}

def organize_files(folder_path, simulate=False):
    """
    Organizes files in the specified folder into subfolders based on file type.
    
    Parameters:
    folder_path (str): The path to the folder containing files to organize.
    simulate (bool): If True, only simulates the organization without making changes.
    """
    # Step(5.1) Initialize a summary counter for each category
    summary = {category: 0 for category in CATEGORIES.keys()}
    summary["Others"] = 0  # For files that don't match any category

    # Step(2) Scan the folder for files only
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories and process files only
        if not os.path.isfile(file_path):
            continue

        # print(f"Found file: {filename}")

        # Determine the file's extension and its category
        extension = os.path.splitext(filename)[1].lower()
        category = next((cat for cat, exts in CATEGORIES.items() if extension in exts), "Others")

        # Define the target directory for the file
        target_dir = os.path.join(folder_path, category)

        if not simulate:
            try:
                # Create the target directory if it doesn't exist
                os.makedirs(target_dir, exist_ok=True)
                # Step(4) Move the file to its respective directory
                shutil.move(file_path, os.path.join(target_dir, filename))
            except PermissionError:
                print(f"Skipping file (permission denied): {filename}")
                continue

        # Update the summary counter for the category
        summary[category] += 1

    # Step(5.2) Print a summary of the organized files
    print("\nSummary of organized files:")
    for category, count in summary.items():
        print(f"{category}: {count} files")


def main():
    """
    Main function to handle user input and initiate the file organization process.
    """
    # Step(1) Accept folder path from command-line arguments or user input
    if len(sys.argv) < 2:
        folder_path = input("Enter folder path: ").strip()
    else:
        folder_path = sys.argv[1]

    # Check for simulation mode flag
    simulate = "--simulate" in sys.argv

    # Validate the provided folder path
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    print(f"Processing folder: {folder_path}")

    # Call the organize_files function to organize the files
    organize_files(folder_path, simulate)


# Running the script
if __name__ == "__main__":
    main()