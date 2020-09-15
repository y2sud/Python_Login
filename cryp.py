from cryptography.fernet import Fernet
import hashlib

#key = Fernet.generate_key()
key = b'-eIrNLRLmLaKUw-yMDKISb1TqtB9TBLSS8WyNRfAgW8='

class Cryp:
    @staticmethod
    def encrypt(plain):
        cypher = Fernet(key).encrypt(plain.encode())
        return cypher

    @staticmethod
    def decrypt(cypher):
        plain = Fernet(key).decrypt(cypher)
        return plain.decode()

    @staticmethod
    def f_hash(plain_password):
        hashed = hashlib.sha256(plain_password.encode()).hexdigest()
        return hashed

    @staticmethod
    def password_match(hashed_password, plain_password):
        return hashed_password == hashlib.sha256(plain_password.encode()).hexdigest()

if __name__ == "__main__":
    encoded_text = Cryp.encrypt('any_db_password').decode()
    print('encoded text ', encoded_text)
    print('decrypted text ', Cryp.decrypt(encoded_text.encode()))
    #hashed = Cryp.f_hash("Messi%")
    #print('hashed text ', hashed)
    #print('password match? ', Cryp.password_match(hashed, "Thisw is all"))

