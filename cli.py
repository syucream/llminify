from typing import Annotated
import typer

from command.minify import run_minify

app = typer.Typer()


def main(path: str, compress: Annotated[bool, typer.Option(help="")] = False):
    run_minify(path, compress)


if __name__ == "__main__":
    typer.run(main)
