from cryptography.fernet import Fernet
import os

f = open("IAM_Keyfile", "w+")
f.write("PD2orjvkSgENTqH8JR8a6jBjldkBmSITz8UQB5mH")
f.close()

### 1. read your password file
with open('IAM_Keyfile') as f:
    mypwd = ''.join(f.readlines())

### 2. generate key and write it in a file
key = Fernet.generate_key()
f = open("referenceKey", "wb")
f.write(key)
f.close()

### 3. encrypt the password and write it in a file
refKey = Fernet(key)
mypwdbyt = bytes(mypwd, 'utf-8') # convert into byte
encryptedPWD = refKey.encrypt(mypwdbyt)
f = open("IAM_Key_Encrypted", "wb")
f.write(encryptedPWD)
f.close()
### 4. delete the password file
if os.path.exists("IAM_Keyfile"):
  os.remove("IAM_Keyfile")
else:
  print("File is not available")
