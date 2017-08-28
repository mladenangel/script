import base64

msg='Hello word from Python'
s_bytes=msg.encode()
enc1 = base64.b64encode(s_bytes)
dec1 = base64.b64decode(enc1)
s_dec1=dec1.decode()
print('Plaintext:',msg)
print('Base64:',enc1)
print('Decoded:',s_dec1)

