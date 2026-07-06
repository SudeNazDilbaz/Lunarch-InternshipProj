import os
import shutil

from secure_uploader.validator import is_allowed_file
from secure_uploader.sanitizer import clean_filename, get_safe_path
from secure_uploader.permissions import set_safe_permissions


def secure_upload(source_file_path, original_filename, upload_dir, allowed_extensions=None):
    
    is_valid, message = is_allowed_file(source_file_path, allowed_extensions)

    if not is_valid:
        return False, f"Upload rejected: {message}"

    os.makedirs(upload_dir, exist_ok=True)

    safe_filename = clean_filename(original_filename)
    destination_path = get_safe_path(upload_dir, safe_filename)

    shutil.copy2(source_file_path, destination_path)

    permission_result = set_safe_permissions(destination_path)

    if not permission_result:
        return False, "Upload failed: permissions could not be applied."

    return True, f"File uploaded successfully: {safe_filename}"