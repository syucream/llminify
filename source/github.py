import os
import requests

from source.utils import is_allowed_filetype, process_ipynb_file


TOKEN = os.getenv("GITHUB_TOKEN", "default_token_here")
if TOKEN == "default_token_here":
    raise EnvironmentError("GITHUB_TOKEN environment variable not set.")

headers = {"Authorization": f"token {TOKEN}"}


def download_file(url, target_path):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    with open(target_path, "wb") as f:
        f.write(response.content)


def process_directory(url: str, output):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    files = response.json()

    for file in files:
        if file["type"] == "file" and is_allowed_filetype(file["name"]):
            print(f"Processing {file['path']}...")

            temp_file = f"temp_{file['name']}"
            download_file(file["download_url"], temp_file)

            output.write(f"# {'-' * 3}\n")
            output.write(f"# Filename: {file['path']}\n")
            output.write(f"# {'-' * 3}\n\n")

            if file["name"].endswith(".ipynb"):
                output.write(process_ipynb_file(temp_file))
            else:
                with open(temp_file, "r", encoding="utf-8", errors="ignore") as f:
                    output.write(f.read())

            output.write("\n\n")
            os.remove(temp_file)
        elif file["type"] == "dir":
            process_directory(file["url"], output)


def process_github_repo(repo_url: str):
    api_base_url = "https://api.github.com/repos/"
    repo_url_parts = repo_url.split("https://github.com/")[-1].split("/")
    repo_name = "/".join(repo_url_parts[:2])

    subdirectory = ""
    if len(repo_url_parts) > 4 and repo_url_parts[2] == "tree":
        subdirectory = "/".join(repo_url_parts[4:])

    contents_url = f"{api_base_url}{repo_name}/contents"
    if subdirectory:
        contents_url = f"{contents_url}/{subdirectory}"

    repo_content: list[str] = []

    def process_directory(url: str, repo_content):
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        files = response.json()

        for file in files:
            if file["type"] == "file" and is_allowed_filetype(file["name"]):
                print(f"Processing {file['path']}...")

                temp_file = f"temp_{file['name']}"
                download_file(file["download_url"], temp_file)

                repo_content.append(f"# {'-' * 3}\n")
                repo_content.append(f"# Filename: {file['path']}\n")
                repo_content.append(f"# {'-' * 3}\n\n")

                if file["name"].endswith(".ipynb"):
                    repo_content.append(process_ipynb_file(temp_file))
                else:
                    with open(temp_file, "r", encoding="utf-8", errors="ignore") as f:
                        repo_content.append(f.read())

                repo_content.append("\n\n")
                os.remove(temp_file)
            elif file["type"] == "dir":
                process_directory(file["url"], repo_content)

    process_directory(contents_url, repo_content)
    print("All files processed.")

    return "\n".join(repo_content)
