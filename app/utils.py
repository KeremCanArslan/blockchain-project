import hashlib

def calculate_hash(file_content):
    return hashlib.sha256(file_content).hexdigest()
