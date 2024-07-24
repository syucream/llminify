import tempfile
from source.localfile import process_local_folder
from transform.check import get_token_count
from transform.preprocess import preprocess_text


def safe_file_read(filepath: str, fallback_encoding="latin1") -> str:
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except UnicodeDecodeError:
        with open(filepath, "r", encoding=fallback_encoding) as file:
            return file.read()


def run_minify(path: str, compress: bool, filename: str | None) -> None:
    if compress:
        filename = filename if filename else "compressed_output.txt"

        with tempfile.NamedTemporaryFile(delete=False) as f:
            process_local_folder(path, f.name)
            preprocess_text(f.name, filename)

        compressed_text = safe_file_read(filename)
        compressed_token_count = get_token_count(compressed_text)
        print(
            f"\n[bright_green]Compressed Token Count:[/bright_green] [bold bright_cyan]{compressed_token_count}[/bold bright_cyan]"
        )
    else:
        filename = filename if filename else "uncompressed_output.txt"

        process_local_folder(path, filename)

        uncompressed_text = safe_file_read(filename)
        uncompressed_token_count = get_token_count(uncompressed_text)
        print(
            f"[bright_green]Uncompressed Token Count:[/bright_green] [bold bright_cyan]{uncompressed_token_count}[/bold bright_cyan]"
        )

    print(
        "\n[bold bright_yellow]compressed_output.txt[/bold bright_yellow] and [bold bright_blue]uncompressed_output.txt[/bold bright_blue] have been created in the working directory."
    )
