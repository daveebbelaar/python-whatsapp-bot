import sys
import os
from dotenv import load_dotenv
from pathlib import Path
import logging


def load_configurations(app):    
    # Determine the base directory
    base_dir = Path(__file__).resolve().parent.parent
    # Construct the full path to the .env file
    env_path = base_dir / '.env'
    # Load the .env file
    load_dotenv(dotenv_path=env_path)
    # load_dotenv()
    app.config["ACCESS_TOKEN"] = os.getenv("ACCESS_TOKEN")
    app.config["YOUR_PHONE_NUMBER"] = os.getenv("YOUR_PHONE_NUMBER")
    app.config["APP_ID"] = os.getenv("APP_ID")
    app.config["APP_SECRET"] = os.getenv("APP_SECRET")
    print("DEBUG: APP_SECRET set to", app.config["APP_SECRET"])
    app.config["RECIPIENT_WAID"] = os.getenv("RECIPIENT_WAID")
    app.config["VERSION"] = os.getenv("VERSION")
    app.config["PHONE_NUMBER_ID"] = os.getenv("PHONE_NUMBER_ID")
    app.config["VERIFY_TOKEN"] = os.getenv("VERIFY_TOKEN")


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )
