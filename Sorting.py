from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
# pip install watchdog for this to work


class MyHandler(FileSystemEventHandler):
    i = 1

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "\\" + filename
            new_destination = folder_destination + "\\" + filename
            os.rename(src, new_destination)


folder_to_track = "C:\\Users\\mjonas\\Desktop\\Test1"
folder_destination = "C:\\Users\\mjonas\\Desktop\\Test2"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()