import typer

from command.minify import run_minify

app = typer.Typer()


@app.command()
def minify(path: str):
    run_minify(path)


@app.command()
def version():
    typer.echo("llminify 0.0.1")


if __name__ == "__main__":
    app()
