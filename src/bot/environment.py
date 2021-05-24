from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN=os.getenv("BOT_TOKEN")
COMMAND_PREFIX=os.getenv("COMMAND_PREFIX")
DESCRIPTION=os.getenv("DESCRIPTION")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST")
DB_NAME=os.getenv("DB_NAME")