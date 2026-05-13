import base64
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend

class EncryptHelper:
    def __init__(self, logger):
        self.logger = logger
        
        self.logger.info("Encryption Helper constructor")

    # Helper function to decrypt a password that has a private key associated to it.
    def decrypt_password(encrypted_b64: str, private_key):
        encrypted_bytes = base64.b64decode(encrypted_b64)
        plaintext = private_key.decrypt(
            encrypted_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return plaintext.decode()
    
    # Helper function to get the private key from the folder.
    def get_priv_key_from_path(self, priv_key_path):
        with open(priv_key_path, "rb") as f:
            key_data = f.read()

        private_key = serialization.load_pem_private_key(
            key_data,
            password=None,
            backend=default_backend()
        )
        return private_key