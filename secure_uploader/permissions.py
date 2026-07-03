import os
import stat


def set_safe_permissions(file_path):
    
    try:
        os.chmod(
            file_path,
            stat.S_IRUSR
            | stat.S_IWUSR
            | stat.S_IRGRP
            | stat.S_IROTH
        )
        return True

    except Exception as error:
        print(f"Permission error: {error}")
        return False