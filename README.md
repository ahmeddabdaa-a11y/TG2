# TG Star Sniper Sustainable

An advanced Telegram Automation System designed with an utmost priority on **Stealth**, **Longevity**, and **Risk Management**.

## Phase 1 Completed Features:
- System Architecture.
- Encrypted Storage Engine (Fernet).
- CLI Menu using `Rich` & `Typer` in Arabic.
- Account Management (Add, List, Vault assignment).
- Proxy Support per account.

## Setup Instructions

1. **Install Requirements:**
   ```bash
   cd tg-star-sniper-sustainable
   pip install -r requirements.txt
   ```

2. **Run the CLI Interface:**
   ```bash
   python main.py
   ```

3. **Master Password:**
   You should set an environment variable for the encryption engine before running in production:
   ```bash
   export MASTER_PASSWORD="MySuperSecretPassword_!"
   ```
