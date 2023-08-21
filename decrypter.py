#! /usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = os.listdir()
targets = []
key = 'key.key'
secret_password = 'hello world'


# Check if key exist in the current directory
if os.path.exists(key):

    print('Please enter secret password:')
    entered_password = input('')

    if secret_password == entered_password:

        # Get encryption key
        with (open(key, 'rb')) as the_key:
            encryption_key = the_key.read()


        # Get all files from the current directory
        for file in files:

            file_extension = os.path.splitext(file)

            # Execlude Python scripts & key from decryption
            if file.lower().endswith(('.py', '.key')):
                continue

            # Execlude directories from decryption
            if os.path.isdir(os.path.abspath(file)):
                continue
            
            targets.append(file)

            with open(file, 'rb') as the_file:
                file_content = the_file.read()

            decrypted_content = Fernet(encryption_key).decrypt(file_content)
            with open(file, 'wb') as the_file:
                the_file.write(decrypted_content)

        # Delete key after decryption
        try:
            os.remove(key)
        except OSError as e:
            print(f"Error in deleting key{e}")


        print('Congratulations ... Your Files Has Been Decrypted Successfully')
    else:
        print('Password is wrong!')
else:
    print('Key is not exist!')






    


    
