import os
from pathlib import Path
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        print(str(Path(base_path) / relative_path))

    return str(Path(base_path) / relative_path)