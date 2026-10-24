import typer
from rich.console import Console
from rich.table import Table
from model import Task
from database import task_list, insert_task, delete_task, update_task, complete_task, statistic
from rich.panel import Panel
from rich.columns import Columns

console=Console()

app=typer.Typer()

@app.command(short_help="Add another work!") 
def add(task: str, category: str):
    typer.echo(f"adding {task},in {category}")
    task=Task(task, category)
    insert_task(task)
    show()

@app.command(short_help="Remove a headload ;)")
def delete(position: int):
    typer.echo(f"deleting {position}")
    delete_task(position-1)
    show()

@app.command(short_help="after position specify task and/or category")
def update(position:int , task:str=None , category:str=None):
    typer.echo(f"updating {position}")
    update_task(position-1, task, category)
    show()

@app.command(short_help="only if u actually did it :D")
def complete(position: int):
    typer.echo(f"completing {position}")
    complete_task(position-1)
    show()

@app.command()
def stats():
    typer.echo("Fetching data")
    statistic()
    total, pending, completed =statistic()
    console.print(Columns([
        Panel(f"{total}", title="TOTAL TASKS", border_style="blue"),
        Panel(f"{pending}", title="PENDING TASKS", border_style="red"),
        Panel(f"{completed}", title="COMPLETED TASKS", border_style="green")
    ]))    


@app.command()
def show(status:int=None):
    tasks=task_list(status)
    console.print("[bold green]Ur Task List[/bold green]","🗒️")

    table=Table(show_header=True, header_style="bold blue")
    table.add_column("Positon",style="dim",width=7)
    table.add_column("[bold blue on orange]Task[/bold blue on orange]", style="u", max_width=25)
    table.add_column("Category", min_width=17 ,style="b",justify="right")
    table.add_column("Status",min_width=14, justify="right")

    def get_category_colour(category):
        COLOURS={'Coding':'cyan', 'Study':'blue','Personal':'magenta'}
        if category in COLOURS:
            return COLOURS[category]
        return "white" 

    for idx, task in enumerate(tasks,start=1):
        c=get_category_colour(task.category)
        is_done_str="✅" if task.status==2 else "❎"
        table.add_row(str(idx),task.task,f'[{c}]{task.category}[/{c}]',is_done_str)
    console.print(table)

if __name__=="__main__":
    app()
 