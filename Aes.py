import binascii,os
import random, string

iv = os.urandom(16)
aes_mode = AES.MODE_CBC
key = ''.join(random.choice(string.ascii_uppercase +
string.ascii_lowercase + string.digits) for _ in range(16))
print(key)
encryptor = AES.new(key, aes_mode, iv)
def aes_encrypt(plaintext):
  plaintext = convert_to_16(plaintext)

  ciphertext = encryptor.encrypt(plaintext)
  return ciphertext

def convert_to_16(plaintext):
  add = 16-(len(plaintext) % 6)
  return(plaintext + ' ' * add)

Encrypted = aes_encrypt('Aangi')
print("Encrypted Message: " , Encrypted)
print("Khandhar Aangi")
