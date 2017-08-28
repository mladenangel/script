import hashlib
import binascii
plaintext = 'hello world from python'
print(plaintext)
# sha1
sha1 = hashlib.sha1()
sha1.update(plaintext.encode())
hash_sha1 = sha1.digest()
hex_hash_sha1 = sha1.hexdigest()
print('hash sha1:', hash_sha1)
print('hex hash sha1:', hex_hash_sha1)
# sha256
sha256 = hashlib.sha256()
sha256.update(plaintext.encode())
hash_sha256 = sha256.digest()
hex_hash_sha256 = sha256.hexdigest()
print('hash sha256:', hash_sha256)
print('hex hash sha256:', hex_hash_sha256)
