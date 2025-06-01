from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ASTRA_DB_ID = os.getenv('ASTRA_DB_ID')
ASTRA_DB_REGION = os.getenv('ASTRA_DB_REGION')
ASTRA_DB_KEYSPACE = os.getenv('ASTRA_DB_KEYSPACE')
ASTRA_DB_APPLICATION_TOKEN = os.getenv('ASTRA_DB_APPLICATION_TOKEN')
