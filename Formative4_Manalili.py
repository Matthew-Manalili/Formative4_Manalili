#!/usr/bin/env python
# coding: utf-8

# In[104]:


def bin_to_dec(binary_string):
    string_of_binary=str(binary_string)
    number_of_digits=len(string_of_binary)
    integer_representation=0
    index_of_exponent=0
    while number_of_digits!=0:
        integer_representation+=int(string_of_binary[number_of_digits-1])*2**(index_of_exponent)
        number_of_digits-=1
        index_of_exponent+=1
    return integer_representation
def dec_to_bin(number):
    index_of_exponent=0
    remainder=1
    binary_string=""
    digits=1
    if number==0:
        return 0
    while 2**index_of_exponent<=number:
        if 2**index_of_exponent==number:
            binary_string+="1"
            while index_of_exponent!=0:
                binary_string+="0"
                index_of_exponent-=1
            break
        elif 2**(index_of_exponent+1)>number:
            remainder=number-2**(index_of_exponent)
            binary_string+="1"
            while remainder!=0:
                if 2**(index_of_exponent-digits)>remainder:
                    binary_string+="0"
                else:
                    binary_string+="1"
                    remainder=remainder-2**(index_of_exponent-digits)
                    if remainder==0:
                        remaining_exponent=index_of_exponent-digits
                        while remaining_exponent!=0:
                            binary_string+="0"
                            remaining_exponent-=1
                digits+=1
            break
        index_of_exponent+=1
    return binary_string
def telephone_cipher(message):
    message=message.upper()
    ciphered_message=""
    letter=""
    encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }
    number_of_letters=len(message)
    to_put_in_index=len(message)
    while to_put_in_index!=0:
        if number_of_letters-to_put_in_index!=0:
            if encoder_dict[message[number_of_letters-to_put_in_index-1]][0]==encoder_dict[message[number_of_letters-to_put_in_index]][0]:
                ciphered_message+="_"
        letter=message[number_of_letters-to_put_in_index]
        ciphered_message+=encoder_dict[letter]
        to_put_in_index-=1
    return ciphered_message
def telephone_decipher(telephone_string):
    deciphered_message=""
    index=0
    letter=""
    decipher_dict = {
        "0":" ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }
    while index!=len(telephone_string):
        if index!=0:
            if telephone_string[index-1]==telephone_string[index]:
                    letter+=telephone_string[index]
            else:
                if index==len(telephone_string)-1:
                    letter+=telephone_string[index]
                else: 
                    if telephone_string[index]==telephone_string[index+1]:
                        letter+=telephone_string[index]
                    else:
                        letter+=telephone_string[index]
        else:
            letter+=telephone_string[index]
                
        if telephone_string[index]!="_":
            if index==len(telephone_string)-1:
                deciphered_message+=decipher_dict[letter]
            else:
                if telephone_string[index]!=telephone_string[index+1]:    
                    deciphered_message+=decipher_dict[letter]
                    letter=""
        else:
            deciphered_message+=""
            letter=""
        index+=1
    return deciphered_message

