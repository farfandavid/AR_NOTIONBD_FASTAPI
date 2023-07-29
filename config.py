import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_TITLE: str = "Jobboard"
    PROJECT_VERSION: str = "0.0.1"
    SECRETKEY: str = os.getenv("SECRETKEY")
    BD_URL: str = os.getenv("BD_URL")


settings = Settings()
