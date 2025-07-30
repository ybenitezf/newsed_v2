"""Application entry point"""

from newseditor.drivers.webapp import web_app_factory
from newseditor.drivers.toga_app import start_gui
from .factories import factory_main

if __name__ == "__main__":
    # setup and cache main app instance
    factory_main()

    # start gui
    start_gui(web_app=web_app_factory).main_loop()

