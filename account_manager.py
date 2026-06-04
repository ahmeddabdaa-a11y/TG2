import os
import json
from telethon import TelegramClient
from telethon.sessions import StringSession
from typing import Optional, Dict
from storage.encryption import EncryptionManager

class AccountManager:
    """
    إدارة حسابات التلجرام، الجلسات، دعم البروكسي (Stealth Engine).
    """
    def __init__(self, storage_path: str, encryption_manager: EncryptionManager):
        self.storage_path = storage_path
        self.encryption_manager = encryption_manager
        
        # إنشاء مسار التخزين إذا لم يكن موجوداً
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        self.accounts = self.load_accounts()

    def load_accounts(self) -> Dict:
        """تحميل الحسابات من الملف المحلي وفك تشفيرها"""
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if 'encrypted_data' in data:
                    try:
                        decrypted = self.encryption_manager.decrypt(data['encrypted_data'].encode('utf-8'))
                        return json.loads(decrypted)
                    except Exception as e:
                        print(f"Error decrypting sessions. Invalid Master Password? Error: {e}")
                        return {}
                return data
        return {}

    def save_accounts(self):
        """تشفير الحسابات وحفظها في التخزين المحلي"""
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            encrypted = self.encryption_manager.encrypt(json.dumps(self.accounts))
            json.dump({'encrypted_data': encrypted.decode('utf-8')}, f)

    async def add_account_step1(self, name: str, api_id: int, api_hash: str, phone: str, proxy: Optional[dict] = None) -> TelegramClient:
        """تهيئة السشن الجديد وطلب الرمز (Step 1)"""
        client = TelegramClient(StringSession(), api_id, api_hash, proxy=proxy)
        await client.connect()
        if not await client.is_user_authorized():
            await client.send_code_request(phone)
        return client

    async def save_client_session(self, client: TelegramClient, name: str, api_id: int, api_hash: str, phone: str, proxy: Optional[dict]):
        """حفظ الجلسة بعد تأكيد الكود (Step 2)"""
        session_str = client.session.save()
        self.accounts[name] = {
            'api_id': api_id,
            'api_hash': api_hash,
            'phone': phone,
            'session': session_str,
            'proxy': proxy,
            'is_vault': False
        }
        self.save_accounts()
        await client.disconnect()

    def get_account_session(self, name: str) -> Optional[dict]:
        return self.accounts.get(name)

    def set_vault_account(self, name: str):
        """تحديد حساب ليكون الحساب المخزني (Vault System)"""
        for acc in self.accounts.values():
            acc['is_vault'] = False
        if name in self.accounts:
            self.accounts[name]['is_vault'] = True
            self.save_accounts()
            return True
        return False
