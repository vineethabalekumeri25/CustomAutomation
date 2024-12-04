import os
import shutil

# Path to your Downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

# Define file types and their corresponding folder names
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".webm"],
    "Archives": [".zip", ".tar", ".gz", ".rar"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Programs": [".exe", ".msi", ".apk"],
    "Other": []
}


# Function to move file to corresponding folder based on extension
def organize_files():
    # Iterate over files in the Downloads folder
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Check which category the file belongs to
        folder_name = "Other"
        for category, extensions in file_types.items():
            if file_extension in extensions:
                folder_name = category
                break

        # Create folder if it doesn't exist
        category_folder = os.path.join(downloads_folder, folder_name)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        # Move file to the respective folder
        shutil.move(file_path, os.path.join(category_folder, filename))
        print(f"Moved: {filename} to {folder_name}/")


if __name__ == "__main__":
    organize_files()