import zipfile


def extract_archive(archive, destination):
    with zipfile.ZipFile(archive, "r") as archive:
        archive.extractall(destination)


if __name__ == "__main__":
    extract_archive("archives/compressed.zip", "files")
