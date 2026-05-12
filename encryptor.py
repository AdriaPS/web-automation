import base64
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

# Load public key
with open(r"RSA_Keys\public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

password = "TEST_PASSWORD"

encrypted = public_key.encrypt(
    password.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

encrypted_b64 = base64.b64encode(encrypted).decode()
print(encrypted_b64)