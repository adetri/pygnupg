import gnupg
import os

gpg = gnupg.GPG(gnupghome='/home/ubuntu/.gnupg')

path ='test_file/'
# ptfile ='/test.txt.enc'

for f in os.listdir(path):
    print(f)
    with open(path + f, 'rb') as ef:
        status = gpg.decrypt_file(ef,passphrase = 'adetri86', output=path +f)
        
    print(status.ok)
    print(status.stderr)
