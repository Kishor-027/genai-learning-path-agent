from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def save_progress(profile: dict, roadmap: list[dict], path: Path) -> dict:
    data = {
        "profile": profile,
        "roadmap": roadmap,
        "saved_at": datetime.now(timezone.utc).isoformat(),
    }
    path.write_text(json.dumps(data, indent=2))
    return data


def load_progress(path: Path) -> dict:
    return json.loads(path.read_text())
