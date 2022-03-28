import os
from dotenv import load_dotenv


def load_env():
    """Load .env file from parent directory if it exists."""
    package_path = os.path.abspath(os.path.dirname(__file__))
    env_path = os.path.join(package_path, "..", ".env")
    if os.path.exists(env_path):
        load_dotenv(dotenv_path=env_path)


load_env()
