import os
from dataclasses import dataclass

@dataclass
class Settings:
    """
    الإعدادات المركزية للمشروع.
    Zero Hardcoded strategy.
    """
    REDIS_HOST: str = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT: int = int(os.getenv('REDIS_PORT', 6379))
    
    # يجب تعيين هذا المتغير في خوادم الإنتاج (Environment Variable)
    MASTER_PASSWORD: str = os.getenv('MASTER_PASSWORD', 'super_secret_encryption_key_123!')
    
    # استراتيجية مزدوجة
    GLOBAL_MARGIN_PERCENT: float = float(os.getenv('GLOBAL_MARGIN_PERCENT', '0.15')) # 15%
    DRAWDOWN_PROTECTION: float = float(os.getenv('DRAWDOWN_PROTECTION', '0.80')) # 80%

config = Settings()
