import gnupg

gpg = gnupg.GPG(gnupghome='/home/ubuntu/.gnupg')
key_data = open('emosi2_pub_key.asc').read()
import_result = gpg.import_keys(key_data)

gpg.trust_keys(import_result.fingerprints,'TRUST_ULTIMATE')

mykeys=gpg.list_keys()

print(mykeys)