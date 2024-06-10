def Shift_upgrade(value, letter):
    # letter = list(input("Enter sentence to shift it's Equivalent integers:> "))
    # value = int(input("Enter the shifting magnitude(integers only):> "))
    # letter = list(letter)  # converting letter to list for easy iterations

    # Writing a for loop to iterate over the letter variable and convert each character of all the words it contain
    list_integers_to_be_shifted = []    # Creating an empty list collect integers to be converted
    shifted_integers = []   # Creating an empty list to collect the integers after shifting operation
    for i in letter:
        converted_integer_value = ord(i)
        # list_integers_to_be_shifted.append(converted_integer_value) # printing the integers to be listed to testing purpose. It is not good to print this out
        shifted_result = value + converted_integer_value
        shifted_integers.append(shifted_result)

    # print(list_integers_to_be_shifted)
    print("-------------------WOW IT WORKED--------------------")
    return shifted_integers


"""
Writing a function to retrieve the ascii or unicode of the shifted integers

The function below takes the output of the shifted_upgrade function as input
"""
def encrypted_result(int_list):

    empty_list = []
    int_list = list(int_list)
    for i in int_list:
        ascii_value = chr(int(i))
        empty_list.append(ascii_value)

    return empty_list


def Decrypting(value, encrypt_text):
    # value = int(input("Enter the same value(integer) used in encryption:> "))
    decrypt_list = []

    for i in encrypt_text:
        decrypt_list.append(ord(i) - value)
        # print(decrypt_list)
    return decrypt_list

# decrypted_text_integers = Decrypting(test_variable)

# Writing a for loop to convert all the integers to their corresponding ascii values
"""
decrypted_list = []
for i in decrypted_text_integers:
  decrypted_list.append(chr(i))

print(decrypted_list) # printing the decrypted text

decrypted_text = ''.join(decrypted_list)

print('----------------------Printing the decrypted text----------------------------')
print(decrypted_text)
"""
