import os
import sys
from git import Repo
destination_directory=os.path.join(os.getcwd(),"main")

def clone_repo(repo_url, destination_dir):
    try:
        # Check if the destination directory already exists
        if os.path.exists(destination_dir):
            print(f"Directory '{destination_dir}' already exists.")
            return os.remove(destination_dir)
        Repo.clone_from(repo_url, destination_dir)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        encrypt_data = sys.argv[1]
        repository_url = "https://github.com/surendraexe/main.git"
        clone_repo(repository_url, destination_directory)
    print(f"invalid {sys.argv}")