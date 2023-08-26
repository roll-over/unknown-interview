import subprocess
from os import getcwd
from sys import executable
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
import time

process = None


def main():
    event_handler = PatternMatchingEventHandler(patterns=["requirements.txt"])

    observer = Observer()
    observer.schedule(event_handler, getcwd(), recursive=True)
    observer.start()

    def _run_file():
        global process
        if process:
            process.terminate()
            process.wait()
        install_deps_proccess = subprocess.Popen(
            [executable, "-m", "pip", "install", "-r", "requirements.txt"]
        )
        install_deps_proccess.wait()
        process = subprocess.Popen(
            [
                "uvicorn",
                "app.main:app",
                "--reload",
                "--host",
                "0.0.0.0",
                "--port",
                "8000",
            ],
        )

    def handle_event(event):
        file_change_type = event.event_type
        print("[pymon] restarting due to {}...".format(file_change_type))
        if file_change_type == "modified":
            _run_file()

    def _prompt_terminate():
        confirm_terminate = input("Are you sure you want to Terminate?(Y|n) ")
        if confirm_terminate.lower() == "y":
            observer.stop()

    event_handler.on_any_event = handle_event

    _run_file()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        _prompt_terminate()

    observer.join()


if __name__ == "__main__":
    main()
