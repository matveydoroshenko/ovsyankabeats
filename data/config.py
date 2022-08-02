import os

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = {
422999166
         }
QIWI_TOKEN = os.getenv("qiwi")
QIWI_PUBKEY = os.getenv("qiwi_p_pub")
WALLET_QIWI = os.getenv("wallet")

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")

