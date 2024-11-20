import pathlib
import zipfile


def make_archive(file_paths, folder_path):
    archive_path = pathlib.Path(folder_path, "archive.zip")

    with zipfile.ZipFile(archive_path, "w") as archive:
        for file_path in file_paths:
            file_path = pathlib.Path(file_path)
            archive.write(file_path, arcname=file_path.name)


if __name__ == "__main__":
    make_archive(["files/a.txt", "files/b.txt", "files/c.txt"], "archives")
