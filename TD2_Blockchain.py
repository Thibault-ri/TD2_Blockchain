import secrets as sc
import hashlib


entropy=str(sc.randbits(128))

print(entropy)

entropy_hash=hashlib.sha256(entropy.encode()).hexdigest()

print(entropy_hash)

