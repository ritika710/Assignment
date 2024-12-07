#Assignment 2
import os
import zipfile
import logging
from pathlib import Path

def zip_folder(folder_path, zip_name=None, password=None):
    try:
        # Check if the folder exists
        folder_path = Path(folder_path)
        if not folder_path.exists() or not folder_path.is_dir():
            raise ValueError("The provided folder path is invalid.")

        # Default zip name is the folder name
        if zip_name is None:
            zip_name = folder_path.name

        zip_file = folder_path.parent / f"{zip_name}.zip"

        # Create a zip file
        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through the directory and add files to the zip
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(folder_path.parent)
                    zipf.write(file_path, arcname)

            logging.info(f"Successfully created zip file: {zip_file}")

        # Password protection feature (optional, requires pyzipper or similar library)
        if password:
            try:
                import pyzipper
                with pyzipper.AESZipFile(zip_file, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
                    for root, dirs, files in os.walk(folder_path):
                        for file in files:
                            file_path = Path(root) / file
                            arcname = file_path.relative_to(folder_path.parent)
                            zipf.write(file_path, arcname)
                    zipf.setpassword(password.encode())
                logging.info(f"Zip file created with password protection: {zip_file}")
            except ImportError:
                logging.warning("pyzipper module not found, skipping password protection.")

        return zip_file

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Input Parsing
    folder_path = input("Enter the path to the folder you want to zip: ").strip()
    
    if not folder_path:
        print("Folder path cannot be empty.")
    else:
        # Custom zip name (Optional)
        zip_name = input("Enter custom name for the zip file (leave empty for default): ").strip() or None

        # Password protection (Optional)
        password = input("Enter a password for the zip file (leave empty for no password): ").strip() or None
        
        # Call the zip_folder function
        zip_file = zip_folder(folder_path, zip_name, password)
        
        if zip_file:
            print(f"Zip file created: {zip_file}")
        else:
            print("Failed to create zip file.")
