import gnupg
import os

gpg = gnupg.GPG(gnupghome='/home/ubuntu/.gnupg')

path ='/home/ubuntu/txtfiles'
ptfile ='/test.txt.enc'

with open(path + ptfile, 'rb') as f:
    status = gpg.decrypt_file(f,passphrase = 'adetri86', output=path +ptfile + ".dec")
    
print(status.ok)
print(status.stderr)
