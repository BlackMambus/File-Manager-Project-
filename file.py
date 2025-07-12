import os
import shutil

def list_files(path):
    print(f"\n📁 Contents of: {path}")
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print(f"[DIR]  {item}")
            else:
                print(f"[FILE] {item}")
    except FileNotFoundError:
        print("❌ Directory not found.")

def create_folder(path, folder_name):
    try:
        os.makedirs(os.path.join(path, folder_name))
        print(f"✅ Folder '{folder_name}' created.")
    except FileExistsError:
        print("⚠️ Folder already exists.")

def delete_item(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
        print(f"🗑️ Folder '{path}' deleted.")
    elif os.path.isfile(path):
        os.remove(path)
        print(f"🗑️ File '{path}' deleted.")
    else:
        print("❌ File or folder not found.")

def move_item(src, dest):
    try:
        shutil.move(src, dest)
        print(f"📦 Moved '{src}' to '{dest}'.")
    except Exception as e:
        print(f"❌ Error: {e}")

def rename_item(src, new_name):
    try:
        base = os.path.dirname(src)
        new_path = os.path.join(base, new_name)
        os.rename(src, new_path)
        print(f"✏️ Renamed to '{new_name}'.")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    while True:
        print("\n=== Python File Manager ===")
        print("1. List files")
        print("2. Create folder")
        print("3. Delete file/folder")
        print("4. Move file/folder")
        print("5. Rename file/folder")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            path = input("Enter directory path: ")
            list_files(path)

        elif choice == "2":
            path = input("Enter parent directory: ")
            folder_name = input("Enter new folder name: ")
            create_folder(path, folder_name)

        elif choice == "3":
            path = input("Enter full path of file/folder to delete: ")
            delete_item(path)

        elif choice == "4":
            src = input("Enter source path: ")
            dest = input("Enter destination path: ")
            move_item(src, dest)

        elif choice == "5":
            src = input("Enter full path of file/folder to rename: ")
            new_name = input("Enter new name: ")
            rename_item(src, new_name)

        elif choice == "6":
            print("👋 Exiting File Manager.")
            break

        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()


