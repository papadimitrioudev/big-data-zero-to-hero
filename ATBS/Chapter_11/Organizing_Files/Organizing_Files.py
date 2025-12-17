import zipfile
import os


def simple_backup(folder_path):
    """
    Creates incremental backups of a folder.
    """
    # Get the folder name from the path
    folder_name = os.path.basename(folder_path)

    # Find next available backup number
    backup_number = 1
    while True:
        zip_name = f"{folder_name}_backup{backup_number}.zip"
        if not os.path.exists(zip_name):
            break
        backup_number += 1

    print(f"Starting backup to: {zip_name}")

    # Create the ZIP file
    file_count = 0
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        # Walk through all files in the folder tree
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Get full path to the file
                full_path = os.path.join(root, file)

                # Add file to the ZIP
                zipf.write(full_path)
                file_count += 1

    print(f"Backup completed: {file_count} files saved to {zip_name}")


# Interactive version
def interactive_backup():
    """
    Interactive backup tool with user prompts.
    """
    print("=== SIMPLE BACKUP TOOL ===")

    # Ask user for folder path
    folder = input("Enter folder path to backup: ").strip()

    # Check if folder exists
    if not os.path.exists(folder):
        print(f"Error: '{folder}' does not exist.")
        return

    # Ask for backup name
    base_name = input("Enter base name for backup (press Enter for default): ").strip()
    if not base_name:
        base_name = "backup"

    # Find next available number
    num = 1
    while True:
        zip_name = f"{base_name}_{num}.zip"
        if not os.path.exists(zip_name):
            break
        num += 1

    print(f"\nCreating: {zip_name}")

    # Create backup
    try:
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path)

        print(f"Το backup δημιουργήθηκε στο: {os.path.abspath(zip_name)}")
    except Exception as e:
        print(f"❌ Backup failed: {e}")


# Run the program
if __name__ == "__main__":
    # Uncomment one of these options:

    # Option 1: Backup specific folder
    # simple_backup(r"C:\Users\YourName\Documents")

    # Option 2: Interactive mode
    interactive_backup()