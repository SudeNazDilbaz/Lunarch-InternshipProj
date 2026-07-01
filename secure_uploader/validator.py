from pathlib import Path

MAGIC_BYTES = {
    b"\xFF\xD8\xFF": ["jpg", "jpeg"],
    b"\x89\x50\x4E\x47": ["png"],
    b"\x25\x50\x44\x46": ["pdf"],
    b"\x4D\x5A": ["exe", "dll"],
}

DEFAULT_ALLOWED_EXTENSIONS = ["jpg", "jpeg", "png", "pdf"]


def is_allowed_file(file_path, allowed_extensions=None):
    """
    Checks whether a file is allowed by using magic byte validation.
    """
    if allowed_extensions is None:
        allowed_extensions = DEFAULT_ALLOWED_EXTENSIONS

    file_path = Path(file_path)

    if not file_path.exists():
        return False, "File does not exist."

    with open(file_path, "rb") as file:
        header = file.read(8)

    for magic, extensions in MAGIC_BYTES.items():
        if header.startswith(magic):
            for ext in extensions:
                if ext in allowed_extensions:
                    return True, ext

            return False, f"This file type is not allowed: {extensions[0]}"

    return False, "Unknown or unsupported file format."