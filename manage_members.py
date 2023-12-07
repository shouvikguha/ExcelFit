import json
import os
import bcrypt

def load_members_from_file(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r') as file:
        return json.load(file)

def save_members_to_file(filename, members):
    with open(filename, 'w') as file:
        json.dump(members, file, indent=4)

def password_hashed(password):
    password_in_bytes = password.encode() # Convert password to bytes and hash it
    return bcrypt.hashpw(password_in_bytes, bcrypt.gensalt())

def add_member(filename, user_name, password):
    members = load_members_from_file(filename)
    if user_name in members:
        return False  # Member in file, member exists
    hashed_password = password_hashed(password)
    members[user_name] = hashed_password.decode() # String hashed password
    save_members_to_file(filename, members)
    return True

def verify_member(filename, user_name, password):
    members = load_members_from_file(filename)
    if user_name not in members:
        return False
    # Hash the entered password and compare with the stored hash
    password_bytes = password.encode()
    stored_password_bytes = members[user_name].encode()
    return bcrypt.checkpw(password_bytes, stored_password_bytes)