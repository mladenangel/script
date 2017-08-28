from Crypto.PublicKey import RSA
from Crypto import Random
from colorama import *
# generate private and public keys
# Then, save them into files
print Fore.RED+Back.WHITE+'generating private and public keys...'+Style.RESET_ALL
key = RSA.generate(2048)
f = open('my_rsa_private_key.pem', 'wb')
f.write(key.exportKey('PEM'))
f.close()
f = open('my_rsa_public_key.pem', 'wb')
f.write(key.publickey().exportKey('PEM'))
f.close()
print Fore.RED+Back.YELLOW+'done'+Style.RESET_ALL
message = 'hello world from python'
print Fore.BLUE+Back.WHITE+'plaintext:', message+Style.RESET_ALL
# encrypt data using public key
f = open('my_rsa_public_key.pem','r')
RSAkey = RSA.importKey(f.read())
f.close()
k = Random.new().read(8)
encrypted_msg = RSAkey.encrypt(message.encode(), k)
ciphertext = encrypted_msg[0]
print 'encrypted:',ciphertext
# decrypt data using private key
f = open('my_rsa_private_key.pem','r')
RSAkey = RSA.importKey(f.read())
f.close()
decrypted_msg = RSAkey.decrypt(ciphertext)
print Fore.YELLOW+Back.RED+'decrypted:', decrypted_msg.decode("utf-8")+Style.RESET_ALL

