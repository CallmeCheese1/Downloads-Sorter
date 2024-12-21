# Downloads Sorter # 

This project is a script that will run in the background, silently, to automatically sort your downloads folder into...

- Images: .jpg, .jpeg, .png, .gif, .webp,
- Documents: .pdf, .docx, .txt,
- Videos: .mp4, .mkx, .avi, .mov,
- Music: .mp3, .wav,
- Executables: .exe,
- Compressed: .7z, .zip,
- Other: .apk, .py, .jar, .html

To run it, use Task Scheduler (on windows) to schedule running DOWNLOADS-SORTER.exe in dist\main on startup. You won't notice a window open; it will lurk within your Task Manager. To cancel the script, find DOWNLOADS-SORTER.exe in Task Manager, and end the task. It's written in upper case for user visibility.

Further image and file formats will be updated as I encounter more unknown formats in my own uses. 