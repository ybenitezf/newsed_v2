from typing import Any
from fasthtml import common as ft
from fasthtml.core import FastHTML
from newseditor.factories import factory_main
from starlette.requests import Request
from .utils import app_from_request

def factory() -> Any:
    """Boot the web app, start dependencies, etc"""
    app = factory_main()
    ft_app: FastHTML
    ft_app, rt = ft.fast_app()
    ft_app.state.editor_app = app

    @rt('/')
    def get(request: Request):
        app = app_from_request(request)
        print(app.get_app_dir())
        return ft.Div(ft.P('Hello World!'), hx_get="/change")

    @rt('/change')
    def change(request: Request):
        app = app_from_request(request)
        print(app.get_app_dir())
        return ft.Div(ft.P('Change'))
    
    return ft_app

def web_app_factory() -> None:
    ft.serve(
        appname="newseditor.drivers.webapp.core",
        app="factory",
        reload=False
    )


if __name__ == "__main__":
    web_app_factory()