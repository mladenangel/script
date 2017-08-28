import hashlib
import binascii
plaintext = 'hello world from python'
print(plaintext)
# hash with key
# hmac
key = 'p4ssw0rd'
hmac = hashlib.pbkdf2_hmac('sha256', key.encode(), plaintext.encode(), 100000)
hex_hash_hmac = binascii.hexlify(hmac)
print('hex hash hmac:', hex_hash_hmac)
