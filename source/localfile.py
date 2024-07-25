from io import TextIOWrapper
import os

from source.utils import is_allowed_filetype, process_ipynb_file


def process_local_directory(
    local_path: str, extensions: list[str], output: TextIOWrapper
):
    for root, dirs, files in os.walk(local_path):
        for file in files:
            if is_allowed_filetype(file, extensions):
                print(f"Processing {os.path.join(root, file)}...")

                output.write(f"# {'-' * 3}\n")
                output.write(f"# Filename: {os.path.join(root, file)}\n")
                output.write(f"# {'-' * 3}\n\n")

                file_path = os.path.join(root, file)

                if file.endswith(".ipynb"):
                    output.write(process_ipynb_file(file_path))
                else:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        output.write(f.read())

                output.write("\n\n")


def process_local_folder(
    local_path: str, extensions: list[str], output_file: str
) -> None:
    if not os.path.exists(local_path):
        raise FileNotFoundError(f"Directory {local_path} does not exist.")

    with open(output_file, "w", encoding="utf-8") as output:
        process_local_directory(local_path, extensions, output)

    print("All files processed.")
