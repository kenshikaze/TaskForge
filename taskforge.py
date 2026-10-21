import typer
from rich.console import Console
from rich.table import Table


console=Console()

app=typer.Typer()

@app.command(short_help="Add another work!") 
def add(task: str, category: str):
    typer.echo(f"adding {task},in {category}")
    show()

@app.command(short_help="Remove a headload ;)")
def delete(position: int):
    typer.echo(f"deleting {position}")
    show()

@app.command(short_help="give ur work an update")
def update(position:int , task:str=None , category:str=None):
    typer.echo(f"updating {position}")
    show()

@app.command(short_help="only if u actually did it ")
def complete(position: int):
    typer.echo(f"completing {position}")
    show()

@app.command()
def show():
    tasks=[("Complete ur project", "Coding"), ("Finish assignments","Study"), ("Buy groceries","Essential works")]
    console.print("[bold green]Ur Task List[/bold green]","🗒️")

    table=Table(show_header=True, header_style="bold blue")
    table.add_column("Positon",style="dim",width=7)
    table.add_column("[bold blue on orange]Task[/bold blue on orange]", style="u", max_width=25)
    table.add_column("Category", min_width=17 ,style="b",justify="right")
    table.add_column("Status",min_width=14, justify="right")

    def get_category_colour(category):
        COLOURS=[('Coding','cyan'), ('Study','blue'), ('Essential works','magenta') ]
        if category in COLOURS:
            return COLOURS[category]
        return "white" 

    for idx, task in enumerate(tasks,start=1):
        c=get_category_colour(task[1])
        is_done_str="✅" if True==2 else "❎"
        table.add_row(str(idx),task[0],f'[{c}]{task[1]}[/{c}]',is_done_str)
    console.print(table)


if __name__=="__main__":
    app()