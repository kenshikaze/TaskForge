import sqlite3
from typing import List
import datetime
from model import task

con=sqlite3.connect("tasks.db")

cur=con.cursor()

def create_table():
    cur.execute(''' 
            CREATE TABLE IF NOT EXISTS tasks (
            task text,
            category text,
            date_added text,
            date-completed text
            status integer
            position integer
            )''')

create_table()

def insert_task(task:task):
    cur.execute('select count(*) FROM tasks')
    count=cur.fetchone()[0]
    task.position =count if count else 0
    with con:
        cur.execute('INSERT INTO tasks VALUES (:task, :category, :date_added, :date_completed, :status, :position)',
                  {'task':task.task, 'category':task.category, 'date_added':task.date_added, 'date_completed':task.date_completed, 'status':task.status, 'position':task.position})

def task_list() -> List[task]:
    cur.execute('select * from tasks')
    results=cur.fetchall()
    tasks=[]
    for result in results:
        tasks.append(task(*result))
    return tasks

