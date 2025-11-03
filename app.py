
import os
import json
import hashlib
import secrets
import argparse

USERS_DIR = "users"

def create_user(username, name, password):
    """Creates a new user and stores their data in a JSON file."""
    if not os.path.exists(USERS_DIR):
        os.makedirs(USERS_DIR)

    user_file = os.path.join(USERS_DIR, f"{username}.json")
    if os.path.exists(user_file):
        print(f"Error: User '{username}' already exists.")
        return

    salt = secrets.token_hex(16)
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()

    user_data = {
        "username": username,
        "name": name,
        "salt": salt,
        "hashed_password": hashed_password,
    }

    with open(user_file, "w") as f:
        json.dump(user_data, f, indent=4)

    print(f"User '{username}' created successfully.")

def login(username, password):
    """Logs in a user by verifying their password."""
    user_file = os.path.join(USERS_DIR, f"{username}.json")
    if not os.path.exists(user_file):
        print(f"Error: User '{username}' not found.")
        return

    with open(user_file, "r") as f:
        user_data = json.load(f)

    salt = user_data["salt"]
    hashed_password = user_data["hashed_password"]

    if hashlib.sha256((password + salt).encode()).hexdigest() == hashed_password:
        print("Login successful!")
    else:
        print("Login failed. Incorrect password.")

def main():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(description="Authentication Module")
    subparsers = parser.add_subparsers(dest="command")

    # Create user command
    create_parser = subparsers.add_parser("create", help="Create a new user")
    create_parser.add_argument("username", help="The username")
    create_parser.add_argument("name", help="The user's name")
    create_parser.add_argument("password", help="The user's password")

    # Login command
    login_parser = subparsers.add_parser("login", help="Login as a user")
    login_parser.add_argument("username", help="The username")
    login_parser.add_argument("password", help="The user's password")

    args = parser.parse_args()

    if args.command == "create":
        create_user(args.username, args.name, args.password)
    elif args.command == "login":
        login(args.username, args.password)
    else:
        parser.print_help()

if __name__ == "__main__":
    if not os.path.exists(USERS_DIR):
        os.makedirs(USERS_DIR)
    main()
