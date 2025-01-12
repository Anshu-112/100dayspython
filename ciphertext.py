logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P___88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P___88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("type 'encode' to encrypt , type 'decode' to decrypt:\n")
text=input("type your message:\n")
shift=int(input("type your shift number:\n"))


def encrypt(original_text,shift_number):
    cipher_text=""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text+=letter
        else:
            shift_position=alphabet.index(letter)+shift_number
            shift_position%=len(alphabet)
            cipher_text+=alphabet[shift_position]
       
    print(f"your encrypted text is {cipher_text}")
def decrypt(encrypt_text,shift_number):
    decrypt_text=""
    for letter in encrypt_text:
        if letter not in alphabet:
            decrypt_text+=letter
        else:
            shift_position=alphabet.index(letter)-shift_number
            shift_position%=len(alphabet)
            decrypt_text+=alphabet[shift_position]
        
    print(f"your decrypted text is {decrypt_text}")

if direction=="encode":
    encrypt(text,shift)
else:
    decrypt(text,shift)        

