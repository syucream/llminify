from nbconvert import PythonExporter
import nbformat


# TODO enable to specify target filetypes at runtime
def is_allowed_filetype(filename):
    allowed_extensions = [
        ".py",
        ".txt",
        ".js",
        ".tsx",
        ".ts",
        ".md",
        ".cjs",
        ".html",
        ".json",
        ".ipynb",
        ".h",
        ".localhost",
        ".sh",
        ".yaml",
        ".example",
    ]
    return any(filename.endswith(ext) for ext in allowed_extensions)


def process_ipynb_file(temp_file):
    with open(temp_file, "r", encoding="utf-8", errors="ignore") as f:
        notebook_content = f.read()

    exporter = PythonExporter()
    python_code, _ = exporter.from_notebook_node(
        nbformat.reads(notebook_content, as_version=4)
    )
    return python_code
