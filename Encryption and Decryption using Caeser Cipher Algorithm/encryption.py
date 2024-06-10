# encryption.py
import time
from relevant_functions import Shift_upgrade, encrypted_result

def encrypt_text():
    print('\t\t\t\t\t\t****Encryption Process****')
    print('>>>>>Hello! Welcome to cipher encryption<<<<<<')
    text= input ("Please Enter The Text You Want encrypted: ")
    shift= int(input("Please Enter Shift Number: "))
    test_variable = Shift_upgrade(shift, text)

    encode=encrypted_result(test_variable)
    shifted_message = ''.join(encode)
    print('Encrypting...........0%')
    time.sleep(3)
    print('Encrypting..........25%')
    time.sleep(3)
    print('Encrypting..........50%')
    time.sleep(3)
    print('Encrypting..........75%')
    time.sleep(3)
    print('Encrypting.........100%')
    time.sleep(2)
    print('----------------------Printing the encrypted text----------------------------')

    print(f"{shifted_message}\n\nEncryption completed! ")

    return shifted_message