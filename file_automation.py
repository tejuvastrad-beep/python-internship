"""
Task 1: Python File Handling & Automation

Objective:
- Read and write TXT and CSV files
- Automate file operations (rename, move, delete)
- Handle errors using try-except
"""

import os
import shutil
import csv

print("=" * 60)
print("        PYTHON FILE HANDLING & AUTOMATION")
print("=" * 60)

try:
    # -------------------------------------------------------
    # Step 1: Create and write to a text file
    # -------------------------------------------------------
    with open("sample.txt", "w") as file:
        file.write("Welcome to Python File Handling!\n")
        file.write("This file was created automatically.\n")
        file.write("Learning automation using Python.\n")

    print("[INFO] sample.txt created successfully.")

    # -------------------------------------------------------
    # Step 2: Read the text file
    # -------------------------------------------------------
    print("\n[INFO] Reading sample.txt...\n")

    with open("sample.txt", "r") as file:
        print(file.read())

    # -------------------------------------------------------
    # Step 3: Create a CSV file
    # -------------------------------------------------------
    students = [
        ["ID", "Name", "Department", "Marks"],
        [1, "Hemant", "CSE", 95],
        [2, "Rahul", "ISE", 87],
        [3, "Anjali", "ECE", 91]
    ]

    with open("data.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(students)

    print("[INFO] data.csv created successfully.")

    # -------------------------------------------------------
    # Step 4: Read the CSV file
    # -------------------------------------------------------
    print("\n[INFO] Reading data.csv...\n")

    with open("data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            print(row)

    # -------------------------------------------------------
    # Step 5: Rename the text file
    # -------------------------------------------------------
    os.rename("sample.txt", "notes.txt")
    print("\n[INFO] sample.txt renamed to notes.txt.")

    # -------------------------------------------------------
    # Step 6: Create a backup folder
    # -------------------------------------------------------
    os.makedirs("backup", exist_ok=True)
    print("[INFO] Backup folder is ready.")

    # -------------------------------------------------------
    # Step 7: Move the renamed file to the backup folder
    # -------------------------------------------------------
    shutil.move("notes.txt", "backup/notes.txt")
    print("[INFO] notes.txt moved to backup folder.")

    # -------------------------------------------------------
    # Step 8: Delete the CSV file
    # -------------------------------------------------------
    os.remove("data.csv")
    print("[INFO] data.csv deleted successfully.")

except FileNotFoundError:
    print("[ERROR] File not found.")

except PermissionError:
    print("[ERROR] Permission denied.")

except Exception as e:
    print("[ERROR] Unexpected Error:", e)

finally:
    print("\n[SUCCESS] Program executed successfully.")
    """
Task 1: Python File Handling & Automation

Objective:
- Read and write TXT and CSV files
- Automate file operations (rename, move, delete)
- Handle errors using try-except
"""

import os
import shutil
import csv

print("=" * 60)
print("        PYTHON FILE HANDLING & AUTOMATION")
print("=" * 60)

try:
    # -------------------------------------------------------
    # Step 1: Create and write to a text file
    # -------------------------------------------------------
    with open("sample.txt", "w") as file:
        file.write("Welcome to Python File Handling!\n")
        file.write("This file was created automatically.\n")
        file.write("Learning automation using Python.\n")

    print("[INFO] sample.txt created successfully.")

    # -------------------------------------------------------
    # Step 2: Read the text file
    # -------------------------------------------------------
    print("\n[INFO] Reading sample.txt...\n")

    with open("sample.txt", "r") as file:
        print(file.read())

    # -------------------------------------------------------
    # Step 3: Create a CSV file
    # -------------------------------------------------------
    students = [
        ["ID", "Name", "Department", "Marks"],
        [1, "Hemant", "CSE", 95],
        [2, "Rahul", "ISE", 87],
        [3, "Anjali", "ECE", 91]
    ]

    with open("data.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(students)

    print("[INFO] data.csv created successfully.")

    # -------------------------------------------------------
    # Step 4: Read the CSV file
    # -------------------------------------------------------
    print("\n[INFO] Reading data.csv...\n")

    with open("data.csv", "r") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            print(row)

    # -------------------------------------------------------
    # Step 5: Rename the text file
    # -------------------------------------------------------
    os.rename("sample.txt", "notes.txt")
    print("\n[INFO] sample.txt renamed to notes.txt.")

    # -------------------------------------------------------
    # Step 6: Create a backup folder
    # -------------------------------------------------------
    os.makedirs("backup", exist_ok=True)
    print("[INFO] Backup folder is ready.")

    # -------------------------------------------------------
    # Step 7: Move the renamed file to the backup folder
    # -------------------------------------------------------
    shutil.move("notes.txt", "backup/notes.txt")
    print("[INFO] notes.txt moved to backup folder.")

    # -------------------------------------------------------
    # Step 8: Delete the CSV file
    # -------------------------------------------------------
    os.remove("data.csv")
    print("[INFO] data.csv deleted successfully.")

except FileNotFoundError:
    print("[ERROR] File not found.")

except PermissionError:
    print("[ERROR] Permission denied.")

except Exception as e:
    print("[ERROR] Unexpected Error:", e)

finally:
    print("\n[SUCCESS] Program executed successfully.")