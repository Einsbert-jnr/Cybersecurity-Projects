# main.py
from encryption import encrypt_text
from decryption import decrypt_text

def main():
    user_need = input("If you want to encrypt a text type ENCRYPT and if you want to decode a text type DECRYPT:> ")
    user_need = user_need.lower()

    if user_need == "encrypt":
        encrypt_text()
    elif user_need == 'decrypt':
        decrypt_text()
    else:
        print('Wrong input, try again')

if __name__ == "__main__":
    main()