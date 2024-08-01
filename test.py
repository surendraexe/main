import os
import stat
import sys
import shutil
from git import Repo

from tds.test import fn

def remove_readonly(func, path, excinfo):
    """Change the file permission to writable and retry removal."""
    os.chmod(path, stat.S_IWRITE)
    func(path)

destination_dir = os.path.join(os.getcwd(), "_internal", "_temp_dir")
main_dir = os.path.join(os.getcwd(), "_internal", "main")
repo_url = "https://github.com/surendraexe/main.git"
try:
    # Check if the destination directory already exists
    if os.path.exists(destination_dir):
        print(f"Directory '{destination_dir}' already exists.")
        os.remove(destination_dir)
    Repo.clone_from(repo_url, destination_dir)
    for i in os.listdir(destination_dir):
        if i == ".git":
            git_dir = os.path.join(destination_dir, i)
            try:
                # Change permission to ensure deletion can occur
                for root, dirs, files in os.walk(git_dir):
                    for file in files:
                        filepath = os.path.join(root, file)
                        os.chmod(filepath, stat.S_IWRITE)
                shutil.rmtree(git_dir, onerror=remove_readonly)
                print(f"Removed '{git_dir}'")
            except Exception as e:
                print(f"Failed to remove '{git_dir}': {e}")
        elif main_dir:
            os.replace(os.path.join(destination_dir, "tds"), os.path.join(destination_dir, "tds"))
            print(fn())
    shutil.rmtree(destination_dir)
except Exception as e:
    print(f"An error occurred: {e}")
