"""Main application facade controller"""

from newseditor.entities.base import AppDirsSetup
from pathlib import Path

class NewsEditorApp:
    """News editor application main"""

    def __init__(self, *, app_dirs: AppDirsSetup) -> None:
        data_dir = Path(app_dirs.user_data_dir)
        data_dir.mkdir(parents=True, exist_ok=True)

        self.data_dir = data_dir


    def get_app_dir(self) -> Path:
        return self.data_dir