from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    id: int
    text: str
    created_at: datetime
    done: bool = False
