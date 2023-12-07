import os

from dotenv import load_dotenv


load_dotenv()
MAX_ROOMS = int(os.getenv("MAX_ROOMS", 3))
MAX_ON_PAGE = int(os.getenv("MAX_ON_PAGE", 20))
