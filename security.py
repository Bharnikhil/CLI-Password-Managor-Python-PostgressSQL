from cryptography.fernet import Fernet
from config import SECRET_KEY

fernet = Fernet(SECRET_KEY)

def encrypt_password(password):
    return fernet.encrypt(password.encode())

def decrypt_password(encrypted_password):
    return fernet.decrypt(encrypted_password).decode()
