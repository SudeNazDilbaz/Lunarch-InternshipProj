from pathlib import Path
from typing import Optional, Union

MAGIC_BYTES: dict[bytes, list[str]] = {
    b"\xFF\xD8\xFF": ["jpg", "jpeg"],
    b"\x89\x50\x4E\x47": ["png"],
    b"\x25\x50\x44\x46": ["pdf"],
    b"\x4D\x5A": ["exe", "dll"],
}

DEFAULT_ALLOWED_EXTENSIONS: list[str] = ["jpg", "jpeg", "png", "pdf"]


def is_allowed_file(
    file_path: Union[str, Path],
    allowed_extensions: Optional[list[str]] = None
) -> tuple[bool, str]:
    """
    Checks whether a file is allowed by comparing its magic byte signature
    with known file type signatures.
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
            for extension in extensions:
                if extension in allowed_extensions:
                    return True, extension

            return False, f"This file type is not allowed: {extensions[0]}"

    return False, "Unknown or unsupported file format."