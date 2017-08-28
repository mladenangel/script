import hashlib
import binascii
plaintext = 'hello world from python'
print(plaintext)
# md5
md5 = hashlib.md5()
md5.update(plaintext.encode())
hash_md5 = md5.digest()
hex_hash_md5 = md5.hexdigest()
print('hash md5:', hash_md5)
print('hex hash md5:', hex_hash_md5)
