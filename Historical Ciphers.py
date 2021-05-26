# Python codes for Substituion Cipher encryption
def substituion_cipher_encrypt(text, shift):

    t = list(text)
    textt=[]
    for i in range(len(t)):

     #Encrypting uppercase characters
       if (t[i].isupper()):
          k = chr((ord(t[i]) + int(shift) - 65) % 26 + 65) 
          textt.append(k)

      # Encrypting lowercase characters
       elif (t[i].islower()):
          k =  chr((ord(t[i]) + int(shift) - 97) % 26 + 97)
          textt.append(k)

      # Checking empty list index 
       else:
         textt.append(" ")

    texttt =""
    return (texttt.join(textt))
 
#checking the substituion_cipher_encrypt function  
substituion_text = input("Please give the plaintext : ")      # input: naz
substituion_shift = input("Please give the shift number : ")  # input: 11


print ("The Ciphertext : ", substituion_cipher_encrypt(substituion_text, substituion_shift)) #output: ylk

# Python codes for Substituion Cipher decryption

def substituion_cipher_decrypt(text, shift):

    t = list(text)
    textt=[]
    for i in range(len(t)):

     #Encrypting uppercase characters
       if (t[i].isupper()):
          k = chr((ord(t[i]) - int(shift) - 65) % 26 + 65) 
          textt.append(k)

      # Encrypting lowercase characters
       elif (t[i].islower()):
          k =  chr((ord(t[i]) - int(shift) - 97) % 26 + 97)
          textt.append(k)

      # Checking empty list index 
       else:
         textt.append(" ")

    texttt =""
    return (texttt.join(textt))

decryption = substituion_cipher_encrypt(substituion_text, substituion_shift)

print ("The Plaintext : ", substituion_cipher_decrypt(decryption, substituion_shift))


# Python codes for Hill Cipher encryption

import numpy as np
def hill_cipher_encrypt(text, key):

  a = len(text)

# Generating vector for the key  
  key_matrix = np.zeros((a,a),dtype=int)
  
# Generating vector for the plaintext
  text_matrix = np.zeros(a,dtype=int).T
  
# Generating vector for the cipher
  cipher_matrix = np.zeros(a,dtype=int).T
  
# Getting key matrix from the key string 
  k = 0
  for i in range(3):
      for j in range(3):
          key_matrix[i, j] = ord(key[k]) % 65
          k += 1 
 
# Getting vector from the text string
  for i in range(3):
      text_matrix[i] = ord(text[i]) % 65
  
# Getting the encrypted vector with key metrix and text matrix
  for i in range(3):
    for j in range(3):
      cipher_matrix[i] += (key_matrix[i, j] * text_matrix[j])
    cipher_matrix[i] = cipher_matrix[i] % 26

# Generating the encrypted text from the encrypted vector
  cipher_text = []
  for i in range(3):
      cipher_text.append(chr(cipher_matrix[i] + 65))
  
    # Returning the ciphertext
  return ("".join(cipher_text))
  
#checking the hill_cipher_encrypt function 
hill_text = input("Please give the plaintext : ")      
hill_key = input("Please give the shift number : ")    
  
print("the ciphertext:", hill_cipher_encrypt(hill_text, hill_key) ) 











