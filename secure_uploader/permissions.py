from pathlib import Path
from typing import Union
import os
import stat


def set_safe_permissions(file_path: Union[str, Path]) -> bool:
    """
    Applies safe file permissions to the uploaded file.
    The owner can read and write the file, while
    other users have read-only access.
    """

    file_path = Path(file_path)

    try:
        os.chmod(
            file_path,
            stat.S_IRUSR
            | stat.S_IWUSR
            | stat.S_IRGRP
            | stat.S_IROTH,
        )
        return True

    except OSError as error:
        print(f"Permission error: {error}")
        return False