import os # --> for file and directory operations
import sys # --> for file operations

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

# Running the script
if __name__ == "__main__":
    main()