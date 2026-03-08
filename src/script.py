# INTENTIONALLY VULNERABLE PYTHON - FOR SECURITY SCANNER TESTING ONLY
# Triggers Bandit findings: hardcoded creds, eval, exec, shell injection,
# SQL injection, weak hashing, pickle deserialization, SSRF, etc.

import os
import hashlib
import pickle
import random
import subprocess
import sqlite3
from http.server import HTTPServer, SimpleHTTPRequestHandler

# B105: Hardcoded passwords
PASSWORD = "SuperSecretPassword123!"
DB_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"
SECRET_KEY = "my-secret-jwt-key-do-not-share"

# B303: Weak hash - MD5
def hash_password_md5(password):
    return hashlib.md5(password.encode()).hexdigest()

# B303: Weak hash - SHA1
def hash_password_sha1(password):
    return hashlib.sha1(password.encode()).hexdigest()

# B307: eval()
def evaluate_expression(expr):
    return eval(expr)

# B102: exec()
def execute_code(code_string):
    exec(code_string)

# B602: subprocess with shell=True
def run_command(user_input):
    return subprocess.call(user_input, shell=True)

# B301: pickle deserialization
def load_data(serialized_data):
    return pickle.loads(serialized_data)

# B608: SQL injection via string formatting
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '%s'" % username
    cursor.execute(query)
    return cursor.fetchone()

# B608: SQL injection via f-string
def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM users WHERE id = {user_id}")
    conn.commit()

# B104: Binding to all interfaces
def start_server():
    server = HTTPServer(("0.0.0.0", 8080), SimpleHTTPRequestHandler)
    server.serve_forever()

# B311: Weak RNG for security
def generate_token():
    return "".join([chr(random.randint(65, 90)) for _ in range(32)])

# B110: Bare except
def unsafe_operation():
    try:
        result = eval("os.system('whoami')")
        return result
    except:
        pass

# B101: Assert for security checks
def check_admin(user):
    assert user.is_admin, "User must be admin"
    return True

# B108: Hardcoded temp directory
def write_temp_file(data):
    with open("/tmp/sensitive_data.txt", "w") as f:
        f.write(data)

# B501: requests with verify=False
def fetch_url(url):
    import requests
    return requests.get(url, verify=False).text

# B506: yaml.load without SafeLoader
def load_yaml(yaml_string):
    import yaml
    return yaml.load(yaml_string)

if __name__ == "__main__":
    db_conn = f"postgresql://admin:{DB_PASSWORD}@localhost:5432/mydb"
    user_expr = input("Enter expression: ")
    print(evaluate_expression(user_expr))
    cmd = input("Enter command: ")
    run_command(cmd)
