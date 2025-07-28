"""Application entry point"""

from newseditor.drivers.webapp import web_app_factory
from newseditor.drivers.toga_app import start_gui

if __name__ == "__main__":
    start_gui(web_app=web_app_factory).main_loop()

