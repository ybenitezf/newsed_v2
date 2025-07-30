from typing import Any
from starlette.requests import Request
from starlette.datastructures import State

from newseditor.adapters.controllers.main import NewsEditorApp

def app_from_request(request: Request) -> NewsEditorApp:
    state: State = request.app.state

    try:
        app = state.editor_app
        if isinstance(app, NewsEditorApp):
            return app
        else:
            raise Exception("No application found")
    except KeyError:
        raise Exception("No application found")