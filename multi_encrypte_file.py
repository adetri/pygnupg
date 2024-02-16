import gnupg
import os

gpg = gnupg.GPG(gnupghome='/home/ubuntu/.gnupg')

path ='test_file/'
# ptfile ='/test.txt'

for f in os.listdir(path):
    print(f)
    with open(path + f, 'rb') as ef:
        status = gpg.encrypt_file(ef,recipients = ['detkid@gm.com'], output=path + f)
    
print(status.ok)
print(status.stderr)
