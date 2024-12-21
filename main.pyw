import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DOWNLOADS_FOLDER = "C:/Users/tomie/Downloads"
SORTED_FOLDERS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkx", ".avi", ".mov"],
    "Music": [".mp3", ".wav"],
    "Executables": [".exe"],
    "Compressed": [".7z", ".zip"],
    "Other": [".apk", ".py", ".jar", ".html"]
}

class DownloadSorter(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(DOWNLOADS_FOLDER):
            file_path = os.path.join(DOWNLOADS_FOLDER, filename)
            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1].lower()
                for folder, extensions in SORTED_FOLDERS.items():
                    if ext in extensions:
                        dest_folder = os.path.join(DOWNLOADS_FOLDER, folder)
                        os.makedirs(dest_folder, exist_ok=True)
                        shutil.move(file_path, os.path.join(dest_folder, filename))
                        break

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(DownloadSorter(), DOWNLOADS_FOLDER, recursive=False)
    observer.start()

    observer.join()