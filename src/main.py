import click
from datetime import datetime
from .storage import load_tasks, save_tasks
from .models import Task

@click.group()
def cli():
    """Simple CLI To-Do App"""

@cli.command()
@click.argument("text")
def add(text):
    tasks = load_tasks()
    new_id = (max([t.id for t in tasks]) + 1) if tasks else 1
    tasks.append(Task(id=new_id, text=text, created_at=datetime.now()))
    save_tasks(tasks)
    click.echo(f"Added task #{new_id}: {text}")

@cli.command()
def list():
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks yet.")
        return
    for t in tasks:
        status = "✔" if t.done else "✗"
        click.echo(f"{t.id:3} [{status}] {t.text} ({t.created_at:%Y-%m-%d %H:%M})")

@cli.command()
@click.argument("task_id", type=int)
def done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t.id == task_id:
            t.done = True
            save_tasks(tasks)
            click.echo(f"Marked task #{task_id} as done.")
            return
    click.echo("Task not found.")

if __name__ == "__main__":
    cli()
