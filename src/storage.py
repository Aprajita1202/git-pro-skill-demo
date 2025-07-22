import json
from pathlib import Path
from datetime import datetime
from .models import Task

DATA_FILE = Path("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []
    raw = json.loads(DATA_FILE.read_text())
    return [
        Task(
            id=item["id"],
            text=item["text"],
            created_at=datetime.fromisoformat(item["created_at"]),
            done=item["done"],
        )
        for item in raw
    ]


def save_tasks(tasks):
    payload = [
        {
            "id": t.id,
            "text": t.text,
            "created_at": t.created_at.isoformat(),
            "done": t.done,
        }
        for t in tasks
    ]
    DATA_FILE.write_text(json.dumps(payload, indent=2))
