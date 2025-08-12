# File Organizer

## Option Chosen
Option 1 - File Organizer

## How to Run the Program

1. **Organize Files Without Simulation Mode**  
   Run the following command to organize files in the specified folder:  
   ```bash
   python main.py \path\to\folder
   ```

2. **Organize Files With Simulation Mode**  
   Run the following command to simulate the organization without making changes:  
   ```bash
   python main.py \path\to\folder --simulate
   ```

3. **Generate Sample Files**  
   To create sample files for testing, run the following command:  
   ```bash
   python generate_samples.py
   ```

   This will create a folder named `Test` with sample files to test the application.

## Language and Tools Used
- **Language:** Python 3.13.1

## Extra Features or Notes
- The program categorizes files into predefined categories (`Images`, `Documents`, `Videos`, and `Others`) based on their extensions.
- The `--simulate` flag allows users to preview the organization process without making any changes to the file system.
- The `generate_samples.py` script provides a quick way to create test files for verifying the functionality of the file organizer.