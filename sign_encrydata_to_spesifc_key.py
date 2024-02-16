import gnupg
import os

gpg = gnupg.GPG(gnupghome='/home/ubuntu/.gnupg')
gpg.encoding = 'utf-8'

path = 'test_file/'
file= 'ubuntu_plain_text.txt'

stream = open(path + file,'rb')

fp = gpg.list_keys(True).fingerprints[0]

edat = gpg.encrypt_file(stream, recipients ='emosi2@gm.com',sign=fp, passphrase='adetri86',output= path + file)

print(edat.ok)
print(edat.stderr)

# print(status.ok)

# print(status.stderr)
