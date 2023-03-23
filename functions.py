import os
from unitsdata import LOCAL_DIR

def get_asset_path(tag: str="icons/icon.png") -> str:
    return os.path.join(LOCAL_DIR, tag)
