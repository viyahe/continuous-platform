from dotenv import load_dotenv
import os

test_env_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path=test_env_path)
