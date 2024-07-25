from typing import Annotated, Optional
import typer

from command.minify import run_minify

app = typer.Typer()


def main(
    path: str,
    compress: Annotated[bool, typer.Option(help="if compress results")] = False,
    write: Annotated[
        Optional[str], typer.Option(help="write results to the file path")
    ] = None,
    extensions: Annotated[
        Optional[str],
        typer.Option(help="comma-separated file extensions, e.g.) js,css"),
    ] = None,
):
    run_minify(path=path, compress=compress, filename=write, extensions_str=extensions)


if __name__ == "__main__":
    typer.run(main)
