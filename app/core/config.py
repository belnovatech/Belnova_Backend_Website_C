from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL")
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
