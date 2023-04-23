import bcrypt
from src.infastructure.config.environment.base import settings

def hash_psw(psw: str) -> bytes:
    byte_psw: bytes = psw.encode('utf-8')
    salt: bytes = settings.SALT.encode('utf-8')
    return bcrypt.kdf(
        byte_psw, salt, 
        desired_key_bytes=32, rounds=50
    )
    
def validate_psw(psw: str, hashed: bytes) -> bool:
    psw = psw.encode('utf-8')
    derived_key = bcrypt.kdf(
        psw, settings.SALT.encode('utf-8'),
        desired_key_bytes=32, rounds=50
    )
    return derived_key == hashed
