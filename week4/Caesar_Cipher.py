"""
Write a Python program to create a Caesar cipher encryption and display input text,
encrypted text and decrypted text.
"""

#funtion to return the Caesar Cipher encrypted text
def Caesar_Cipher_enc(text, step):
    enc = ""
    for char in text:
            if char.isalpha():
                encode = ord(char) +step
                if encode > 122:
                    encode -= 26
                elif  (encode>91) and (encode<97):
                    encode -= 26
            else:
                encode  = char
            enc +=  chr(encode)
    return enc

#funtion to return the Caesar Cipher decrypted text
def Caesar_Cipher_de(text, step):
    dec = ""
    for char in text:
            if char.isalpha():
                decode = ord(char) - step
                if decode < 65:
                    decode += 26
                elif  (decode<97) and (decode>91):
                    decode += 26
            else:
                decode  = ord(char)

            dec += chr(decode)
    return dec


# Testing the funtion
otext = input("Enter original text: ") #abc
entext = Caesar_Cipher_enc(otext,2) #cde
print("The Encrypted text: ", entext) 
detext = Caesar_Cipher_de(entext,2) #abc
print("The Decrypted text: ", detext)


