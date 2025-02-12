import os
import sqlite3
import hashlib

# Getting sensitive data from environment variables without proper validation
db_password = os.getenv('DB_PASSWORD')
api_key = os.getenv('API_KEY')

# Connecting to an SQLite database without any encryption or parameterized queries
conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Using raw SQL queries directly from user input (SQL Injection risk)
def fetch_user_data(user_id):
    cursor.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
    return cursor.fetchall()

# Storing passwords directly in the database without hashing
def store_password(username, password):
    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
    conn.commit()

# Storing sensitive data in plain text (API key)
def store_api_key(username, api_key):
    cursor.execute(f"UPDATE users SET api_key = '{api_key}' WHERE username = '{username}'")
    conn.commit()

# Storing sensitive data in logs
def log_user_activity(user_id, action):
    with open('activity.log', 'a') as log_file:
        log_file.write(f"User {user_id} performed action: {action}\n")

# Weak password handling
def weak_password_check(password):
    if len(password) < 6:
        print("Password is too short!")
        return True
    return False

# Saving user password without proper hashing
def create_user(username, password):
    if weak_password_check(password):
        return
    store_password(username, password)

# Insecure password hashing method (MD5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Hardcoding API key in the script


# Not sanitizing user input for file access (path traversal vulnerability)
def read_file(user_input):
    with open(f'/home/user/{user_input}', 'r') as file:
        return file.read()

# Executing untrusted code (remote code execution risk)
def run_untrusted_code(user_input):
    exec(user_input)

# Not checking user input length (could lead to buffer overflow or resource exhaustion)
def process_input(user_input):
    while len(user_input) < 1000:
        user_input += 'A'  # Can lead to resource exhaustion

# Poor key storage (saving API keys in environment variables without encryption)
os.environ['API_KEY'] = api_key
