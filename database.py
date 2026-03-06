import sqlite3
from cryptography.fernet import Fernet

# Function to generate a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)
    return key

# Function to load the encryption key
def load_key():
    return open('secret.key', 'rb').read()

# Function to encrypt the card data
def encrypt_card_data(card_data):
    key = load_key()
    f = Fernet(key)
    encrypted_data = f.encrypt(card_data.encode())
    return encrypted_data

# Function to create a database connection
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

# Function to store encrypted card data in SQLite database
def store_card_data(conn, encrypted_data):
    sql = ''' INSERT INTO cards(data)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (encrypted_data,))
    conn.commit()
    return cur.lastrowid

# Main function to demonstrate usage
if __name__ == '__main__':
    database = 'cards.db'

    # Generate key the first time
    generate_key()  # Uncomment if you need to generate a new key

    # Create a database connection
    conn = create_connection(database)

    # Example card data
    card_data = '1234-5678-9012-3456'
    encrypted_data = encrypt_card_data(card_data)

    # Store encrypted card data
    store_card_data(conn, encrypted_data)
    print('Card data encrypted and stored successfully.')