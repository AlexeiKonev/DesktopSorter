import os
import shutil
from datetime import datetime

def organize_files_on_desktop():
    desktop_path = os.path.expanduser("~/Desktop")  # Путь к рабочему столу
    files = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]

    for file in files:
        file_path = os.path.join(desktop_path, file)
        modification_time = os.path.getmtime(file_path)
        date = datetime.fromtimestamp(modification_time)
        year, month = date.year, date.month

        # Создание папок, если они не существуют
        year_folder = os.path.join(desktop_path, str(year))
        month_folder = os.path.join(year_folder, f"{month:02d}")

        if not os.path.exists(year_folder):
            os.makedirs(year_folder)

        if not os.path.exists(month_folder):
            os.makedirs(month_folder)

        # Перемещение файла в соответствующую папку
        new_file_path = os.path.join(month_folder, file)
        shutil.move(file_path, new_file_path)
        print(f"Файл {file} перемещен в {year}/{month:02d}.")

if __name__ == "__main__":
    organize_files_on_desktop()
