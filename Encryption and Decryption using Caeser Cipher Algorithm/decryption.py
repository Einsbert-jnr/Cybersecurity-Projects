# decryption.py
import time
from relevant_functions import Decrypting

def decrypt_text():
    print('\t\t\t\t\t\t****Decryption Process****')
    print('>>>>>Hello! Welcome to cipher decryption<<<<<<')
    encrypted_text = input("Please Enter The Encrypted Text You Want Decrypted: ")
    shift = int(input("Please Enter Shift Number: "))

    decode = Decrypting(shift, encrypted_text)

    decrypted_list = []
    for i in decode:
        decrypted_list.append(chr(i))

    decrypted_text = ''.join(decrypted_list)
    print('Decrypting...........0%')
    time.sleep(3)
    print('Decrypting..........25%')
    time.sleep(3)
    print('Decrypting..........50%')
    time.sleep(3)
    print('Decrypting..........75%')
    time.sleep(3)
    print('Decrypting.........100%')
    time.sleep(2)

    print('----------------------Printing the decrypted text----------------------------')
    print(f"{decrypted_text}\n\nDecryption completed! ")

    return decrypted_text