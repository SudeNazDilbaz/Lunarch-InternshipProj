import re
from pathlib import Path
from typing import Union


def clean_filename(filename: str) -> str:
    """
    Cleans a filename by removing path traversal expressions
    and replacing unsafe characters with underscores.
    """
    filename = filename.strip()
    
    filename = (
        filename
        .replace("../", "")
        .replace("..\\", "")
        .replace("./", "")
        .replace(".\\", "")
    )

    filename = re.sub(r"[^a-zA-Z0-9._-]", "_", filename)

    filename = filename.strip(". ")

    if not filename:
        return "safe_file"

    return filename


def get_safe_path(upload_dir: Union[str, Path], filename: str) -> Path:
    """
    Generates a safe file path inside the upload directory.
    Raises ValueError if path traversal is detected.
    """

    upload_dir = Path(upload_dir).resolve()

    safe_name = clean_filename(filename)

    full_path = (upload_dir / safe_name).resolve()

    if upload_dir not in full_path.parents and full_path != upload_dir:
        raise ValueError("Invalid file path detected.")

    return full_path