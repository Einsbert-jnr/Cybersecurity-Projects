import time
from relevant_functions import Shift_upgrade, encrypted_result, Decrypting
#Ask the user if they want to encrypt a text or decrypt a text
user_need=input("if you want to encrypt a text type ENCRYPT and if you want to decode a text type DECRYPT:> ")

user_need=user_need.lower()
#Encrypt or decrypt based on the user input

if user_need=="encrypt":
    global shift, test_variable, shifted_message
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
#decryption
elif user_need=='decrypt':
    print('\t\t\t\t\t\t****Decryption Process****')
    print('>>>>>Hello! Welcome to cipher decryption<<<<<<')
    # text= input ("Please Enter The Text You Want decrypted: ")
    # shift= int(input("Please Enter Shift Number: "))
    # test_variable = Shift_upgrade(shift, text)

    encode=encrypted_result(test_variable)

    decode=Decrypting(shift, encode)

    decrypted_list = []
    for i in decode:
        decrypted_list.append(chr(i))

    # print(f"List of decrypting characters: {decrypted_list}") # printing the decrypted text

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
    print(f"{shifted_message} ---> {decrypted_text}\n\nDecryption completed! ")
else:
    print('wrong input try again')