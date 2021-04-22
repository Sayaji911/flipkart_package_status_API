from typing import Dict

import scrapper as _scrapper

def get_current_status(track_id : str):
    return _scrapper.current_status(track_id)
