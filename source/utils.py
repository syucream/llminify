import os
from nbconvert import PythonExporter
import nbformat


DEFAULT_ALLOWED_EXTENSIONS = [
    "py",
    "txt",
    "js",
    "tsx",
    "ts",
    "md",
    "cjs",
    "html",
    "json",
    "ipynb",
    "h",
    "localhost",
    "sh",
    "yaml",
    "example",
]


# TODO enable to specify target filetypes at runtime
def is_allowed_filetype(filename: str, extensions: list[str] = []) -> bool:
    if len(extensions) == 0:
        extensions = DEFAULT_ALLOWED_EXTENSIONS

    fn, extension = os.path.splitext(filename)
    return any(extension == "." + ext for ext in extensions)


def process_ipynb_file(temp_file):
    with open(temp_file, "r", encoding="utf-8", errors="ignore") as f:
        notebook_content = f.read()

    exporter = PythonExporter()
    python_code, _ = exporter.from_notebook_node(
        nbformat.reads(notebook_content, as_version=4)
    )
    return python_code
