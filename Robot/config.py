from dataclasses import dataclass
from pathlib import Path

@dataclass
class BaseConfig:
    base_url: str
    user_data_file: Path
    headless: bool