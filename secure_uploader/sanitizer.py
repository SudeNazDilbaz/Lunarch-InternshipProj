import os
import re

def clean_filename(filename):
    
    filename = filename.replace("../", "").replace("..\\", "")
    filename = filename.replace("./", "").replace(".\\", "")

    filename = re.sub(r"[^a-zA-Z0-9.\-_]", "_", filename)

    filename = filename.strip(". ")

    if not filename:
        filename = "safe_file"

    return filename

def get_safe_path(upload_dir, filename):
    
    safe_name = clean_filename(filename)
    full_path = os.path.join(upload_dir, safe_name)

    upload_dir_abs = os.path.abspath(upload_dir)
    full_path_abs = os.path.abspath(full_path)

    if not full_path_abs.startswith(upload_dir_abs):
        raise ValueError("Invalid file path detected.")

    return full_path_abs