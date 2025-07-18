"""
My first application
"""

import time
from typing import Callable
import toga
from toga.widgets.webview import WebView
from toga.window import MainWindow
import multiprocessing


class HelloWorld(toga.App):
    web_app: Callable[..., None]
    _web_thread: multiprocessing.Process | None

    def __init__(self, *args, **kwargs):
        in_web_app: Callable[..., None] | None = kwargs.pop("web_app")
        assert in_web_app is not None
        self.web_app = in_web_app
        self._web_thread = None
        self.web_view = WebView()

        super().__init__(*args, **kwargs)

    def startup(self):
        self.main_window = MainWindow(title=self.formal_name)
        self.main_window.content = self.web_view
        self.main_window.show()

    async def on_running(self) -> None:
        print("Toga app started")
        if self._web_thread is None:
            self._web_thread = multiprocessing.Process(
                target=self.web_app
            )
            self._web_thread.start()
            time.sleep(0.3)
            print("web app started")
            self.web_view.url = "http://127.0.0.1:5001/"
        return

    async def on_exit(self) -> bool:
        print("Toga app exiting")
        if self._web_thread is not None:
            self._web_thread.terminate()
            time.sleep(0.3)
            print("web app terminated")
        return True

def main(web_app: Callable[..., None]):
    return HelloWorld(web_app=web_app)
