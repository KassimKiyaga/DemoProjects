import hashlib
import sqlite3
from getpass import getpass

# Initialize database
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT,
            security_question TEXT,
            security_answer_hash TEXT
        )
    """)
    conn.commit()
    conn.close()

# Hash function
def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Register new user
def register_user():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    username = input("Enter a username: ")
    password = getpass("Enter a password: ")
    security_question = input("Set a security question: ")
    security_answer = getpass("Enter answer to security question: ")
    
    cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)",
                   (username, hash_text(password), security_question, hash_text(security_answer)))
    conn.commit()
    conn.close()
    print("User registered successfully!")

# Password recovery function
def recover_password():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    username = input("Enter your username: ")
    cursor.execute("SELECT security_question, security_answer_hash FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    if user:
        print("Security Question:", user[0])
        answer = getpass("Enter your answer: ")
        if hash_text(answer) == user[1]:
            cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
            password_hash = cursor.fetchone()[0]
            print("Your password hash is:", password_hash)
        else:
            print("Incorrect answer. Access denied.")
    else:
        print("User not found.")
    
    conn.close()

# Main function
def main():
    init_db()
    while True:
        print("\n1. Register User\n2. Recover Password\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            register_user()
        elif choice == "2":
            recover_password()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
