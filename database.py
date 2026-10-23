import sqlite3
from typing import List
import datetime
from model import Task

con=sqlite3.connect("tasks.db")

cur=con.cursor()

def create_table():
    cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
            task text,
            category text,
            date_added text,
            date_completed text,
            status integer,
            position integer
            )""")

create_table()

def insert_task(task:Task):
    cur.execute('select count(*) FROM tasks')
    count=cur.fetchone()[0]
    task.position =count if count else 0
    with con:
        cur.execute('INSERT INTO tasks VALUES (:task, :category, :date_added, :date_completed, :status, :position)',
                  {'task':task.task, 'category':task.category, 'date_added':task.date_added, 'date_completed':task.date_completed, 'status':task.status, 'position':task.position})

def task_list() -> List[Task]:
    cur.execute('select * from tasks')
    results=cur.fetchall()
    tasks=[]
    for result in results:
        tasks.append(Task(*result))
    return tasks


def delete_task(position):
    cur.execute("select count(*) from tasks")
    count =cur.fetchone()[0]

    with con:
        cur.execute("DELETE from tasks WHERE position=:position",{"position":position})
        for pos in range(position+1, count):
            change_position(pos, pos-1, False)

def change_position(old_position:int, new_position:int, commit=True):
    cur.execute('UPDATE tasks SET position=:position_new WHERE position=:position_old',
                {"position_old":old_position, "position_new":new_position})

    if commit:
        con.commit()

def update_task(position:int, task:str, category:str):
    with con:
        if task is not None and category is not None:
            cur.execute("UPDATE tasks SET task=:task, category=:category WHERE position=:position",
                        {"task":task, "category":category, "position":position})
        elif task is not None:
            cur.execute("UPDATE tasks SET task=:task WHERE position=:position",
                        {"task":task, "position":position})
        elif category is not None:
            cur.execute("UPDATE tasks SET category=:category WHERE position=:position",
                        {"category":category, "position":position})

def complete_task(position:int):
    with con:
        cur.execute("UPDATE tasks SET status=2, date_completed= :date_completed WHERE position= :position",
                    {"position":position, "date_completed":datetime.datetime.now().isoformat()})