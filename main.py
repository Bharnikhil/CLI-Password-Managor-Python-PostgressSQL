import argparse
from db import add_account, get_account
from security import encrypt_password, decrypt_password

def main():
    parser = argparse.ArgumentParser(description="CLI Password Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add account
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("website")
    add_parser.add_argument("username")
    add_parser.add_argument("password")

    # Get account
    get_parser = subparsers.add_parser("get")
    get_parser.add_argument("website")

    args = parser.parse_args()

    if args.command == "add":
        encrypted = encrypt_password(args.password)
        add_account(args.website, args.username, encrypted)
        print("✅ Account added.")

    elif args.command == "get":
        result = get_account(args.website)
        if result:
            username, encrypted_pw = result
            decrypted = decrypt_password(bytes(encrypted_pw))

            print(f"🔐 Username: {username}, Password: {decrypted}")
        else:
            print("❌ No account found.")

if __name__ == "__main__":
    main()
