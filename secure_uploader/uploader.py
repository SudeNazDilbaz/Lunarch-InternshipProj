from pathlib import Path
from typing import Optional, Union
import shutil

from secure_uploader.validator import is_allowed_file
from secure_uploader.sanitizer import clean_filename, get_safe_path
from secure_uploader.permissions import set_safe_permissions


def secure_upload(source_file_path: Union[str, Path],original_filename: str,
upload_dir: Union[str, Path],allowed_extensions: Optional[list[str]] = None,) -> tuple[bool, str]:
    """
    Securely uploads a file by validating its type,
    sanitizing its filename, copying it to the upload
    directory, and applying safe file permissions.
    """

    source_file_path = Path(source_file_path)
    upload_dir = Path(upload_dir)

    is_valid, message = is_allowed_file(
        source_file_path,
        allowed_extensions
    )

    if not is_valid:
        return False, f"Upload rejected: {message}"

    upload_dir.mkdir(parents=True, exist_ok=True)

    safe_filename = clean_filename(original_filename)

    destination_path = get_safe_path(upload_dir, safe_filename)

    shutil.copy2(source_file_path, destination_path)

    if not set_safe_permissions(destination_path):
        return False, "Upload failed: permissions could not be applied."

    return True, f"File uploaded successfully: {safe_filename}"