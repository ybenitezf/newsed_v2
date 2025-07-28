from typing import Any
from fasthtml import common as ft

def factory() -> Any:
    """Boot the web app, start dependencies, etc"""
    app,rt = ft.fast_app()

    @rt('/')
    def get(): return ft.Div(ft.P('Hello World!'), hx_get="/change")

    @rt('/change')
    def change(): return ft.Div(ft.P('Change'))
    
    return app

def web_app_factory() -> None:
    print("Starting web server")
    ft.serve(
        appname="newseditor.drivers.webapp.core",
        app="factory",
        reload=False
    )


if __name__ == "__main__":
    web_app_factory()