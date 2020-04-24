from cryptography.fernet import Fernet


def getkey():
    with open('/var/www/FPSU/FPSU/static/key.key', 'rb') as f:
        key = f.read()
    return key


def encrypt_string(string):
    f = Fernet(getkey())
    return f.encrypt(string)


def decrypt_string(encrypted_str):
    f = Fernet(getkey())
    return f.decrypt(encrypted_str)
