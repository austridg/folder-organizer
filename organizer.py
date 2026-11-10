import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".heic"},
    "Documents": {".pdf", ".doc", ".docx", ".odt", ".txt", ".md", ".rtf",".xls", ".xlsx", ".ods", ".csv", ".ppt", ".pptx", ".odp"},
    "Audio": {".mp3", ".wav", ".flac", ".ogg", ".m4a", ".aac"},
    "Video": {".mp4", ".mkv", ".mov", ".avi", ".webm"},
    "Archives": {".zip", ".tar", ".gz", ".xz", ".bz2", ".7z", ".rar"},
    "Installers": {".rpm", ".deb", ".appimage", ".flatpakref", ".iso", ".exe", ".msi"},
    "Code": {".py", ".js", ".html", ".css", ".json", ".sh", ".c", ".cpp", ".java"},
}

OTHER = "Other"

PARTIAL_SUFFIXES = {".part", ".crdownload", ".tmp"}

def get_category(file_path):
    suffix = file_path.suffix.lower()

    for category, extensions in CATEGORIES.items():
        if suffix in extensions:
            return category

    return OTHER

def unique_destination(destination):
    if not destination.exists():
        return destination

    counter = 1

    while True:

        new_destination = destination.with_name(f"{destination.stem}({counter}){destination.suffix}")

        if not new_destination.exists():

            return new_destination

        counter += 1

def should_skip(file_path):
    if file_path.name.startswith("."):
        return True
    return file_path.suffix.lower() in PARTIAL_SUFFIXES

def organize(folder):

    moved = 0

    for item in sorted(folder.iterdir()):

        if not item.is_file() or should_skip(item):

            continue

        category = get_category(item)

        destination = unique_destination(folder / category / item.name)

        destination.parent.mkdir(exist_ok=True)

        shutil.move(item, destination)

        print(f"{item.name} -> {destination}")

        moved += 1

    return moved

def main():
    parser = argparse.ArgumentParser(description="Organizes the files in a folder.")

    parser.add_argument("folder",nargs="?",type=Path,default=Path.home() / "Documents",help="Just put the folder in the argument, it's not rocket science.")

    args = parser.parse_args()

    folder = args.folder.expanduser().resolve()

    if not folder.is_dir():
        parser.error("Not a directory you idiot!")

    count = organize(folder)
    print(f"Moved {count} files in {folder}")


if __name__ == "__main__":
    main()