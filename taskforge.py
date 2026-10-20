import typer
from rich.console import Console
from rich.table import Table


console=Console()

app=typer.Typer()

@app.command(short_help="Add another work!") 
def add(task: str, category: str):
    typer.echo(f"adding {task},in {category}")

@app.command(short_help="Remove a headload ;)")
def delete(position: int):
    typer.echo(f"deleting {position}")


if __name__=="__main__":
    app()