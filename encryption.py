import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class EncryptionManager:
    """
    نظام التشفير لحماية مفاتيح الـ API و الـ Sessions الخاصة بالحسابات.
    Zero Hardcoded Concept: Key is derived from a master password.
    """
    def __init__(self, password: str, salt: bytes = b'tg_star_sniper_sustainable_salt'):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))
        self.fernet = Fernet(key)

    def encrypt(self, data: str) -> bytes:
        """تشفير النصوص"""
        return self.fernet.encrypt(data.encode('utf-8'))

    def decrypt(self, token: bytes) -> str:
        """فك تشفير النصوص"""
        return self.fernet.decrypt(token).decode('utf-8')
