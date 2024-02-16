import gnupg
import os
# Set the directory where GPG will store its data
gnupghome = '/home/emosi2/.gnupg'

# Ensure the directory exists
if not os.path.exists(gnupghome):
    os.makedirs(gnupghome)

# Create a GPG object
gpg = gnupg.GPG(gnupghome=gnupghome)

# Set encoding
gpg.encoding = 'utf-8'

# Generate key input
input_data = gpg.gen_key_input(
    name_email='emosi2@gm.com',
    passphrase='adetri86',  # Corrected parameter name
    key_type='RSA',
    key_length=1024
)

# Generate the key
key = gpg.gen_key(input_data)
print(key)

pub_key= gpg.export_keys(str(key))

with open('emosi2_pub_key.asc','w')as f:
    f.write(pub_key)
