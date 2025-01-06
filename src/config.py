"""Configuration file for the project."""
import os

from dotenv import load_dotenv

load_dotenv()
BLOCKFRONT_PATH = os.environ.get("BLOCKFRONT_PATH")
NEOFORGE_PATH = os.environ.get("NEOFORGE_PATH")
