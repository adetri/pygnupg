import gnupg
import os

gpg = gnupg.GPG(gnupghome='/home/ubuntu/.gnupg')

path ='/home/ubuntu/txtfiles'
ptfile ='/test.txt'

with open(path + ptfile, 'rb') as f:
    status = gpg.encrypt_file(f,recipients = ['emosi2@gm.com'], output=path +ptfile + ".enc")
    
print(status.ok)
print(status.stderr)
