import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DB_CONN = os.environ.get("DB_CONN")
VAULT_TOKEN = os.environ.get("VAULT_TOKEN")