from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()
class hash():
    def hash_password(password: str):
        return password_hash.hash(password)
    
    def verify(hashed_password , plain_password):
        return password_hash.verify(hashed_password , plain_password)