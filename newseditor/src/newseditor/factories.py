"""Build application and setup dependencies"""
from functools import lru_cache
from newseditor.adapters.controllers.main import NewsEditorApp
from appdirs import AppDirs

@lru_cache(maxsize=1)
def factory_main() -> NewsEditorApp:
    # load config, setup main application instance, etc.
    app_dirs = AppDirs(appname="NewsEditor")
    return NewsEditorApp(app_dirs=app_dirs)