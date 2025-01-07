import random 
import string 

chars = " " + string.punctuation + string.digits + string.ascii_letters 
chars = list(chars) 
key = chars.copy() 

random.shuffle(key) 

plain_text = input("Enter a message to be encrypted : ") 
cipher_text = " " 

for letter in plain_text: 
  index = chars.index(letter)
  cipher_text += key[index] 

print(f"The original message is : {plain_text} ") 
print(f"The encrypted message is : {cipher_text} ") 


cipher_text = input("Enter a message to be decrypted : ") 
plain_text = " " 

for letter in cipher_text: 
  index = key.index(letter) 
  plain_text += chars[index] 

print(f"The original message is : {cipher_text} ") 
print(f"The message after decryption is : {plain_text} ") 


