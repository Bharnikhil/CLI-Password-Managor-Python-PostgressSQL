import psycopg2
from config import DB_CONFIG
"""
DB_CONFIG: Comes from config.py — it's a dictionary with keys like "host", "database", "user", and "password".
"""

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

    """
    **DB_CONFIG unpacks the dictionary and passes it like:

    psycopg2.connect(host="localhost", database="your_db", user="postgres", password="...")
    """

def add_account(website, username, encrypted_password):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO accounts (website, username, password_encrypted) VALUES (%s, %s, %s)",
                (website, username, encrypted_password)
            )

def get_account(website):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT username, password_encrypted FROM accounts WHERE website = %s",
                (website,)
            )
            return cur.fetchone()
