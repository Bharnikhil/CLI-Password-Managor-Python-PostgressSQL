# 🔐 CLI Password Manager

A simple and secure **command-line password manager** built using **Python**, **PostgreSQL**, and **Fernet symmetric encryption** from the `cryptography` library.  
It allows you to **add** and **retrieve** encrypted credentials for different websites through the terminal.

---
```
## 📁 Project Structure
CLI Pass Manager/
├── main.py # CLI interface and command parser
├── db.py # Handles DB connection and account operations
├── security.py # Password encryption and decryption
├── config.py # DB credentials and Fernet secret key
├── README.md # Documentation
└── venv/ # Virtual environment (optional)

```
---

## 🗃️ Database Schema

Table Name: `accounts`

| Column Name        | Data Type     | Description                          |
|--------------------|---------------|--------------------------------------|
| `id`               | SERIAL (PK)   | Auto-incremented ID                  |
| `website`          | TEXT          | Website name (e.g., google, github)  |
| `username`         | TEXT          | Username or email for the account    |
| `password_encrypted`| BYTEA        | Encrypted password (Fernet)          |

---

## 🔄 Workflow of the Project

1. User runs the script using `python main.py`.
2. The CLI uses `argparse` to detect the command: `add` or `get`.
3. For **add**:
   - User inputs `website`, `username`, and `password`.
   - Password is encrypted using `Fernet`.
   - All values are stored in the PostgreSQL database.
4. For **get**:
   - User inputs the `website`.
   - Corresponding record is fetched.
   - Password is decrypted and displayed.

---

## 🔐 About the Encryption

This project uses **Fernet encryption**, which is a form of **symmetric encryption** —  
the same key is used to **encrypt** and **decrypt** the passwords.

---

## 🚀 How to Run

1. **Install Dependencies:**

```bash
pip install psycopg2 cryptography

2.Configure Database and Secret Key:

Update the config.py file:
DB_CONFIG = {
    "host": "localhost",
    "database": "your_db_name",
    "user": "your_username",
    "password": "your_password"
}

SECRET_KEY = b'your-generated-fernet-key'  # Generate once and paste here
Run Commands:

Add an account:


python main.py add google john123 mysecurepass
Get credentials:


python main.py get google
🧩 Problems Faced & Fixes
1. ❌ Not connecting to the database
Problem:
Database connection was failing.

Fix:
Double-check credentials in config.py:

host

database name

username

password

Also ensure your PostgreSQL server is running.

2. ⚠️ TypeError: token must be bytes or str
Problem:
While decrypting passwords during the get operation, this error occurred.

Reason:
The stored password was fetched as a memoryview object instead of raw bytes, which Fernet does not accept.

Fix Options:

In main.py, wrap the encrypted password as bytes(encrypted_pw)


decrypted = decrypt_password(bytes(encrypted_pw))
OR

Handle this directly in security.py, like:


def decrypt_password(encrypted_password):
    return fernet.decrypt(bytes(encrypted_password)).decode()
💡 Tech Stack
Python 3.10+

PostgreSQL (psycopg2)

Cryptography (Fernet symmetric encryption)

argparse (for CLI)

✅ Features
Add new account credentials

Retrieve stored credentials by website

Secure password encryption & storage

Simple and clean CLI experience

📌 Future Improvements
Add delete/update functionality

Add password generator

Add UI (Tkinter/Flask)

Store credentials per user using login system

📃 License
MIT License — feel free to use, modify, and improve.

🙋 About Me
Nikhil Bhardwaj
📧 nbhardwaj502mi@gmail.com

A passionate Python developer interested in building secure tools, learning data science, and exploring new technologies.