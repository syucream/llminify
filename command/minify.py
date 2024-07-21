from source.localfile import process_local_folder
from transform.check import get_token_count
from transform.preprocess import preprocess_text


def safe_file_read(filepath, fallback_encoding="latin1"):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except UnicodeDecodeError:
        with open(filepath, "r", encoding=fallback_encoding) as file:
            return file.read()


def run_minify(path: str):
    output_file = "uncompressed_output.txt"
    processed_file = "compressed_output.txt"

    process_local_folder(path, output_file)

    preprocess_text(output_file, processed_file)

    compressed_text = safe_file_read(processed_file)
    compressed_token_count = get_token_count(compressed_text)
    print(
        f"\n[bright_green]Compressed Token Count:[/bright_green] [bold bright_cyan]{compressed_token_count}[/bold bright_cyan]"
    )

    uncompressed_text = safe_file_read(output_file)
    uncompressed_token_count = get_token_count(uncompressed_text)
    print(
        f"[bright_green]Uncompressed Token Count:[/bright_green] [bold bright_cyan]{uncompressed_token_count}[/bold bright_cyan]"
    )

    print(
        "\n[bold bright_yellow]compressed_output.txt[/bold bright_yellow] and [bold bright_blue]uncompressed_output.txt[/bold bright_blue] have been created in the working directory."
    )
