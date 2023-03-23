import os
import sys

# > Info
VERSION = "0.1.0-alpha"

# > Settings
WINDOW_TITLE = f"MeSure v{VERSION}"
WINDOW_SIZE = (350, 650)

# > Others
LOCAL_DIR = os.path.dirname(__file__) \
    if os.path.basename(sys.executable).startswith("python") \
    else os.path.dirname(sys.executable)