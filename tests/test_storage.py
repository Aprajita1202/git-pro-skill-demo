import os
from pathlib import Path
from src.storage import load_tasks, save_tasks, DATA_FILE
from src.models import Task
from datetime import datetime

def setup_function():
    if Path(DATA_FILE).exists():
        os.remove(DATA_FILE)

def test_roundtrip():
    tasks = [Task(id=1, text="demo", created_at=datetime(2025, 7, 1))]
    save_tasks(tasks)
    loaded = load_tasks()
    assert len(loaded) == 1
    assert loaded[0].text == "demo"
