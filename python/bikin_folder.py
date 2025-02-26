import os

def create_folder(path):
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Folder created at: {path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Base path where you want to create the folders
base_path = "d:\Dev\Learn\python"

# List of folders to create with their subfolders
folders = {
    "LINGKUNGAN": ["C1", "C2", "C3", "C4"],
    "PERSONEL": ["A1", "A2"],
    "PROSEDUR": ["D1", "D2"],
    "FASILITAS": ["B1", "B2", "B3", "B4", "B5"]
}

# Create each folder and its subfolders
for folder, subfolders in folders.items():
    folder_path = os.path.join(base_path, folder)
    create_folder(folder_path)
    for subfolder in subfolders:
        subfolder_path = os.path.join(folder_path, subfolder)
        create_folder(subfolder_path)