import json
from pathlib import Path
from datetime import datetime
from .models import Task

DATA_FILE = Path("tasks.json")


def _task_from_dict(item: dict) -> Task:
    """Convert a stored dict back into a Task object."""
    return Task(
        id=item["id"],
        text=item["text"],
        created_at=datetime.fromisoformat(item["created_at"]),
        done=item["done"],
    )


def _task_to_dict(t: Task) -> dict:
    """Convert a Task to a serializable dict."""
    return {
        "id": t.id,
        "text": t.text,
        "created_at": t.created_at.isoformat(),
        "done": t.done,
    }


def load_tasks():
    if not DATA_FILE.exists():
        return []
    raw = json.loads(DATA_FILE.read_text())
    return [_task_from_dict(item) for item in raw]


def save_tasks(tasks):
    payload = [_task_to_dict(t) for t in tasks]
    DATA_FILE.write_text(json.dumps(payload, indent=2))
